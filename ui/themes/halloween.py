"""Warm Halloween theme with pumpkin, ember, and midnight tones."""

from ui.themes._dark_palette import build_stylesheet


def stylesheet():
    return build_stylesheet(
        background="#100907", card="#21110C", surface="#35190D",
        primary="#E85D24", primary_hover="#B84218", primary_pressed="#6E220E",
        accent="#FFC15E", text="#FFF1D6", muted_text="#C9A98C",
    )
