import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtWidgets import QApplication

# This must run before importing UI/backend modules, which import yt_dlp.
from backend.ytdlp_updater import enable_runtime_package

enable_runtime_package()

from backend.version import APP_NAME, CURRENT_VERSION
from ui.main_window import MainWindow
from ui.resources import APP_ICON


def main():

    # Enable High-DPI icons (Qt 6)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    app = QApplication(sys.argv)

    app.setApplicationName(APP_NAME)
    app.setApplicationDisplayName(APP_NAME)
    app.setApplicationVersion(CURRENT_VERSION)

    app.setWindowIcon(QIcon(str(APP_ICON)))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
