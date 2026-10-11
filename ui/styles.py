from ui.themes.dark import stylesheet as dark_theme
from ui.themes.emerald import stylesheet as emerald_theme
from ui.themes.onyx import stylesheet as onyx_theme
from ui.themes.halloween import stylesheet as halloween_theme
from ui.themes.christmas import stylesheet as christmas_theme
from ui.themes.cyberpunk import stylesheet as cyberpunk_theme
from ui.themes.light import stylesheet as light_theme


def load_styles(theme="dark"):

    themes = {
        "dark": dark_theme,
        "emerald": emerald_theme,
        "onyx": onyx_theme,
        "halloween": halloween_theme,
        "christmas": christmas_theme,
        "cyberpunk": cyberpunk_theme,
        "light": light_theme,
    }

    return themes.get(theme, dark_theme)()
