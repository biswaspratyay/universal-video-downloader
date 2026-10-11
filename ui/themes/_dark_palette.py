"""Shared Qt stylesheet builder for the application's dark color themes."""


def build_stylesheet(
    *,
    background: str,
    card: str,
    surface: str,
    primary: str,
    primary_hover: str,
    primary_pressed: str,
    accent: str,
    text: str,
    muted_text: str,
) -> str:
    return f"""
QMainWindow, QWidget {{ background: {background}; color: {text}; font-family: "Segoe UI"; font-size: 10pt; }}
QMenuBar, QMenu, QStatusBar {{ background: {card}; border-color: {primary_hover}; }}
QMenuBar {{ border-bottom: 1px solid {primary_hover}; }}
QStatusBar {{ border-top: 1px solid {primary_hover}; }}
QMenuBar::item {{ background: transparent; padding: 8px 14px; margin: 4px; border-radius: 6px; }}
QMenuBar::item:selected, QMenu::item:selected {{ background: {primary_hover}; color: {text}; }}
QMenu {{ border: 1px solid {primary_hover}; padding: 6px; }}
QMenu::item {{ padding: 8px 28px; border-radius: 6px; }}
QGroupBox {{ background: {card}; border: 1px solid {primary_hover}; border-radius: 12px; margin-top: 8px; padding: 10px; font-size: 14px; font-weight: 700; }}
QGroupBox::title {{ color: {accent}; left: 16px; padding: 0 6px; subcontrol-origin: margin; background: {background}; }}
QLabel {{ background: transparent; border: none; padding: 0; color: {text}; }}
QLineEdit, QComboBox, QListWidget {{ background: {surface}; color: {text}; border: 1px solid {primary_hover}; border-radius: 8px; padding: 8px; selection-background-color: {primary}; selection-color: {text}; }}
QLineEdit:focus, QComboBox:focus {{ border: 2px solid {primary}; }}
QComboBox::drop-down {{ border: none; width: 28px; }}
QComboBox::down-arrow {{ image: none; }}
QPushButton {{ background: {primary}; color: {text}; border: none; border-radius: 8px; padding: 10px 18px; font-weight: 600; min-height: 18px; }}
QPushButton:hover {{ background: {primary_hover}; }}
QPushButton:pressed {{ background: {primary_pressed}; }}
QPushButton:disabled {{ background: {primary_pressed}; color: {muted_text}; }}
QCheckBox {{ spacing: 8px; background: transparent; }}
QCheckBox::indicator {{ width: 18px; height: 18px; }}
QListWidget {{ outline: none; }}
QListWidget::item {{ padding: 8px; border-radius: 6px; }}
QListWidget::item:hover {{ background: {primary_pressed}; }}
QListWidget::item:selected {{ background: {primary}; color: {text}; }}
QProgressBar {{ border: none; background: {surface}; border-radius: 10px; text-align: center; min-height: 24px; font-weight: 600; color: {text}; }}
QProgressBar::chunk {{ background: {primary}; border-radius: 10px; }}
QFrame {{ background: {background}; border: none; }}
QScrollBar:vertical, QScrollBar:horizontal {{ background: {card}; border: none; }}
QScrollBar:vertical {{ width: 10px; }}
QScrollBar:horizontal {{ height: 10px; }}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {{ background: {primary_hover}; border-radius: 5px; min-height: 30px; min-width: 30px; }}
QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {{ background: {primary}; }}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0; }}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical, QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{ background: none; }}
QToolTip {{ background: {card}; color: {text}; border: 1px solid {accent}; padding: 6px; border-radius: 6px; }}
QFrame#HeaderFrame {{ background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {card}, stop:1 {surface}); border: 1px solid {primary_hover}; border-radius: 18px; }}
QFrame#HeaderNoteFrame {{ border-color: {primary_hover}; }}
QFrame#StatsContainer {{ background: {card}; border: 1px solid {primary_hover}; border-radius: 12px; padding: 8px; }}
QFrame#StatCard {{ background: transparent; border: 1px solid {primary_pressed}; border-radius: 10px; padding: 6px 8px; }}
QLabel#StatLabel {{ color: {muted_text}; font-size: 11px; font-weight: 700; background: transparent; border: none; }}
QLabel#StatValue {{ color: {accent}; font-size: 11px; font-weight: 700; background: transparent; border: none; }}
QFrame#PlatformDetection {{ background: {card}; border: 1px solid {primary_hover}; border-radius: 8px; }}
QLabel#PlatformDetectionTitle {{ color: {muted_text}; font-size: 11px; font-weight: 700; }}
QLabel#PlatformDetectionValue {{ color: {accent}; font-size: 12px; font-weight: 700; }}
QLabel#PlaylistDetectedValue {{ color: {primary}; font-size: 12px; font-weight: 700; }}
"""
