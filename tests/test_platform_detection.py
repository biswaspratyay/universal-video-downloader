import unittest

import backend.platform_utils as platform_utils
from ui.main_window import MainWindow


class PlatformDetectionTests(unittest.TestCase):
    def test_detects_youtube_urls(self):
        self.assertEqual(
            MainWindow._detect_platform("https://www.youtube.com/watch?v=abc123"),
            "YouTube",
        )
        self.assertEqual(
            MainWindow._detect_platform("https://youtu.be/abc123"),
            "YouTube",
        )

    def test_recognizes_youtube_playlist_urls(self):
        self.assertTrue(
            MainWindow._is_youtube_playlist_url(
                "https://youtube.com/playlist?list=PL123"
            )
        )
        self.assertTrue(
            MainWindow._is_youtube_playlist_url(
                "https://www.youtube.com/playlist/?list=PL123&index=1"
            )
        )
        self.assertTrue(
            MainWindow._is_youtube_playlist_url(
                "https://www.youtube.com/watch?v=abc123&list=PL123"
            )
        )
        self.assertTrue(
            MainWindow._is_youtube_playlist_url(
                "https://music.youtube.com/watch?v=abc123&list=PL123"
            )
        )
        self.assertFalse(
            MainWindow._is_youtube_playlist_url(
                "https://example.com/playlist?list=PL123"
            )
        )

    def test_detects_instagram_urls(self):
        self.assertEqual(
            MainWindow._detect_platform("https://www.instagram.com/reel/example/"),
            "Instagram",
        )

    def test_ignores_unknown_and_lookalike_hosts(self):
        self.assertIsNone(MainWindow._detect_platform("https://example.com/video"))
        self.assertIsNone(
            MainWindow._detect_platform("https://notyoutube.com/watch?v=abc123")
        )

    def test_finds_platform_ffmpeg_bundle_in_subdirectory(self):
        ffmpeg_root = __import__("pathlib").Path("/tmp/ffmpeg-root")
        win_dir = ffmpeg_root / "windows"
        win_dir.mkdir(parents=True, exist_ok=True)
        (win_dir / "ffmpeg.exe").touch()
        (win_dir / "ffprobe.exe").touch()

        original_resource_path = platform_utils.resource_path
        original_is_windows = platform_utils.is_windows
        original_is_linux = platform_utils.is_linux
        original_is_macos = platform_utils.is_macos

        try:
            platform_utils.resource_path = lambda relative: ffmpeg_root if relative == "ffmpeg" else original_resource_path(relative)
            platform_utils.is_windows = lambda: True
            platform_utils.is_linux = lambda: False
            platform_utils.is_macos = lambda: False

            self.assertEqual(
                platform_utils.get_ffmpeg_executable(),
                win_dir / "ffmpeg.exe",
            )
            self.assertEqual(
                platform_utils.get_ffprobe_executable(),
                win_dir / "ffprobe.exe",
            )
            self.assertEqual(platform_utils.get_ffmpeg_location(), str(win_dir))
        finally:
            platform_utils.resource_path = original_resource_path
            platform_utils.is_windows = original_is_windows
            platform_utils.is_linux = original_is_linux
            platform_utils.is_macos = original_is_macos


if __name__ == "__main__":
    unittest.main()
