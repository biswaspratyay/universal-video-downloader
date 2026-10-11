"""Winter Pine & Cranberry Christmas theme."""

from ui.themes._dark_palette import build_stylesheet


def stylesheet():
    return build_stylesheet(
        background="#07130E", card="#10291E", surface="#163C2B",
        primary="#1E7A4C", primary_hover="#155B39", primary_pressed="#0D3823",
        accent="#D9B85D", text="#FFF8E7", muted_text="#B6CBBF",
    )
