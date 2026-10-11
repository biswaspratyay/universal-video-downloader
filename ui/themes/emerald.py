"""Emerald-and-gold dark theme for Universal Video Downloader."""


def stylesheet():
    return """
/* A deliberately restrained palette: emerald surfaces dominate; gold is for emphasis. */
QMainWindow, QWidget {
    background: #020906;
    color: #F1F1EA;
    font-family: "Segoe UI";
    font-size: 10pt;
}

QMenuBar, QMenu, QStatusBar {
    background: #052822;
    border-color: #106E54;
}
QMenuBar { border-bottom: 1px solid #106E54; }
QStatusBar { border-top: 1px solid #106E54; }
QMenuBar::item { background: transparent; padding: 8px 14px; margin: 4px; border-radius: 6px; }
QMenuBar::item:selected, QMenu::item:selected { background: #106E54; color: #F1F1EA; }
QMenu { border: 1px solid #106E54; padding: 6px; }
QMenu::item { padding: 8px 28px; border-radius: 6px; }

QGroupBox {
    background: #052822;
    border: 1px solid #106E54;
    border-radius: 12px;
    margin-top: 8px;
    padding: 10px;
    font-size: 14px;
    font-weight: 700;
}
QGroupBox::title {
    color: #DEAA6B;
    left: 16px;
    padding: 0 6px;
    subcontrol-origin: margin;
    background: #020906;
}
QLabel { background: transparent; border: none; padding: 0; color: #F1F1EA; }

QLineEdit, QComboBox, QListWidget {
    background: #03392C;
    color: #F1F1EA;
    border: 1px solid #106E54;
    border-radius: 8px;
    padding: 8px;
    selection-background-color: #119B6D;
    selection-color: #F1F1EA;
}
QLineEdit:focus, QComboBox:focus { border: 2px solid #119B6D; }
QComboBox::drop-down { border: none; width: 28px; }
QComboBox::down-arrow { image: none; }

QPushButton {
    background: #119B6D;
    color: #F1F1EA;
    border: none;
    border-radius: 8px;
    padding: 10px 18px;
    font-weight: 600;
    min-height: 18px;
}
QPushButton:hover { background: #106E54; }
QPushButton:pressed { background: #094E3C; }
QPushButton:disabled { background: #094E3C; color: #8AB0AF; }

QCheckBox { spacing: 8px; background: transparent; }
QCheckBox::indicator { width: 18px; height: 18px; }
QListWidget { outline: none; }
QListWidget::item { padding: 8px; border-radius: 6px; }
QListWidget::item:hover { background: #094E3C; }
QListWidget::item:selected { background: #119B6D; color: #F1F1EA; }

QProgressBar {
    border: none;
    background: #03392C;
    border-radius: 10px;
    text-align: center;
    min-height: 24px;
    font-weight: 600;
    color: #F1F1EA;
}
QProgressBar::chunk { background: #119B6D; border-radius: 10px; }
QFrame { background: #020906; border: none; }

QScrollBar:vertical, QScrollBar:horizontal { background: #052822; border: none; }
QScrollBar:vertical { width: 10px; }
QScrollBar:horizontal { height: 10px; }
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #106E54; border-radius: 5px; min-height: 30px; min-width: 30px;
}
QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover { background: #119B6D; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0; }
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { background: none; }

QToolTip {
    background: #052822;
    color: #F1F1EA;
    border: 1px solid #DEAA6B;
    padding: 6px;
    border-radius: 6px;
}
QFrame#HeaderFrame {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #052822, stop:1 #03392C);
    border: 1px solid #106E54;
    border-radius: 18px;
}
QFrame#HeaderNoteFrame { border-color: #106E54; }
QFrame#StatsContainer {
    background: #052822;
    border: 1px solid #106E54;
    border-radius: 12px;
    padding: 8px;
}
QFrame#StatCard { background: transparent; border: 1px solid #094E3C; border-radius: 10px; padding: 6px 8px; }
QLabel#StatLabel { color: #A49356; font-size: 11px; font-weight: 700; background: transparent; border: none; }
QLabel#StatValue { color: #DEAA6B; font-size: 11px; font-weight: 700; background: transparent; border: none; }
QFrame#PlatformDetection { background: #052822; border: 1px solid #106E54; border-radius: 8px; }
QLabel#PlatformDetectionTitle { color: #8AB0AF; font-size: 11px; font-weight: 700; }
QLabel#PlatformDetectionValue { color: #DEAA6B; font-size: 12px; font-weight: 700; }
QLabel#PlaylistDetectedValue { color: #119B6D; font-size: 12px; font-weight: 700; }
"""
