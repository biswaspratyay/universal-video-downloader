"""Runtime updater for the yt-dlp package.

The packaged application cannot safely overwrite its own bundled Python files
while it is running.  Instead, an updated official wheel is installed in the
user's application-data directory and preferred on the next launch.
"""

from __future__ import annotations

import os
import shutil
import sys
import tempfile
import zipfile
from hashlib import sha256
from pathlib import Path

import requests
from PySide6.QtCore import QObject, Signal, Slot


PYPI_PROJECT_URL = "https://pypi.org/pypi/yt-dlp/json"
TRUSTED_DOWNLOAD_HOSTS = ("files.pythonhosted.org", "pypi.org")


def runtime_package_directory() -> Path:
    """Return the directory whose contents provide the updated package."""
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    else:
        base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    return base / "UniversalVideoDownloader" / "yt-dlp"


def enable_runtime_package() -> None:
    """Prefer a previously downloaded yt-dlp wheel, if it is complete."""
    package_root = runtime_package_directory()
    if (package_root / "yt_dlp" / "__init__.py").is_file():
        package_root_text = str(package_root)
        if package_root_text not in sys.path:
            sys.path.insert(0, package_root_text)


class YtDlpUpdateWorker(QObject):
    """Fetch and install the newest official yt-dlp wheel off the UI thread."""

    completed = Signal(str, str)  # installed version, previous version
    already_current = Signal(str)
    error = Signal(str)
    finished = Signal()

    @Slot()
    def run(self) -> None:
        try:
            import yt_dlp

            current_version = getattr(yt_dlp.version, "__version__", "unknown")
            payload = self._get_release_metadata()
            latest_version = str(payload.get("info", {}).get("version", "")).strip()
            if not latest_version:
                raise RuntimeError("The update service did not provide a valid version.")

            if self._versions_match(latest_version, current_version):
                self.already_current.emit(current_version)
                return

            wheel_url, expected_digest = self._find_universal_wheel(payload, latest_version)
            self._install_wheel(wheel_url, expected_digest, latest_version)
            self.completed.emit(latest_version, current_version)
        except requests.RequestException:
            self.error.emit("Could not reach the yt-dlp update service. Check your internet connection and try again.")
        except (OSError, RuntimeError, zipfile.BadZipFile) as error:
            self.error.emit(f"yt-dlp could not be updated: {error}")
        except Exception:
            self.error.emit("yt-dlp could not be updated. Please try again later.")
        finally:
            self.finished.emit()

    @staticmethod
    def _get_release_metadata() -> dict:
        response = requests.get(PYPI_PROJECT_URL, timeout=20)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            raise RuntimeError("The update service returned invalid data.")
        return payload

    @staticmethod
    def _versions_match(first: str, second: str) -> bool:
        """Compare yt-dlp's date versions despite optional zero padding."""
        try:
            return tuple(int(part) for part in first.split(".")) == tuple(
                int(part) for part in second.split(".")
            )
        except ValueError:
            return first == second

    @staticmethod
    def _find_universal_wheel(payload: dict, version: str) -> tuple[str, str]:
        releases = payload.get("releases", {})
        files = releases.get(version, []) if isinstance(releases, dict) else []
        for file_info in files:
            filename = str(file_info.get("filename", ""))
            url = str(file_info.get("url", ""))
            digest = str(file_info.get("digests", {}).get("sha256", ""))
            if filename.endswith("py3-none-any.whl") and url.startswith("https://"):
                from urllib.parse import urlparse

                if urlparse(url).hostname in TRUSTED_DOWNLOAD_HOSTS and len(digest) == 64:
                    return url, digest
        raise RuntimeError("No compatible official yt-dlp update was found.")

    @staticmethod
    def _install_wheel(wheel_url: str, expected_digest: str, version: str) -> None:
        target = runtime_package_directory()
        target.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="yt-dlp-update-", dir=target.parent) as temp_dir:
            temp_path = Path(temp_dir)
            wheel_path = temp_path / "yt-dlp.whl"
            with requests.get(wheel_url, stream=True, timeout=60) as response:
                response.raise_for_status()
                with wheel_path.open("wb") as wheel_file:
                    for chunk in response.iter_content(chunk_size=1024 * 128):
                        if chunk:
                            wheel_file.write(chunk)

            digest = sha256(wheel_path.read_bytes()).hexdigest()
            if digest.lower() != expected_digest.lower():
                raise RuntimeError("The downloaded yt-dlp file failed its integrity check.")

            staged = temp_path / "package"
            with zipfile.ZipFile(wheel_path) as wheel:
                if any(Path(member.filename).is_absolute() or ".." in Path(member.filename).parts for member in wheel.infolist()):
                    raise RuntimeError("The downloaded yt-dlp package contains an unsafe file path.")
                wheel.extractall(staged)
            if not (staged / "yt_dlp" / "__init__.py").is_file():
                raise RuntimeError("The downloaded file is not a valid yt-dlp package.")

            backup = target.parent / f"yt-dlp-backup-{version}"
            if backup.exists():
                shutil.rmtree(backup)
            if target.exists():
                target.replace(backup)
            try:
                staged.replace(target)
            except OSError:
                if backup.exists() and not target.exists():
                    backup.replace(target)
                raise
            shutil.rmtree(backup, ignore_errors=True)
