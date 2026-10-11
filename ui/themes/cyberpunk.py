"""Neon cyberpunk theme with deep city-night surfaces."""

from ui.themes._dark_palette import build_stylesheet


def stylesheet():
    return build_stylesheet(
        background="#080713",
        card="#121027",
        surface="#1B1740",
        primary="#00E5FF",
        primary_hover="#B026FF",
        primary_pressed="#59208A",
        accent="#FF3CAC",
        text="#F5F3FF",
        muted_text="#A99DC7",
    )
