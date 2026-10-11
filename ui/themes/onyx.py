"""Premium Midnight Onyx & Champagne theme."""

from ui.themes._dark_palette import build_stylesheet


def stylesheet():
    return build_stylesheet(
        background="#0B0B0D", card="#17171B", surface="#242329",
        primary="#D6B46A", primary_hover="#B9944F", primary_pressed="#76582C",
        accent="#E8D19A", text="#F5F1E8", muted_text="#9A9AA0",
    )
