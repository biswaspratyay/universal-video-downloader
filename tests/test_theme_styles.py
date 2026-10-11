from ui.styles import load_styles


def test_light_theme_stylesheet_contains_brand_colors():
    stylesheet = load_styles("light")

    assert "#3B82F6" in stylesheet
    assert "#F8FAFC" in stylesheet
    assert "#0F172A" in stylesheet


def test_emerald_theme_stylesheet_contains_requested_palette():
    stylesheet = load_styles("emerald")

    for color in ("#020906", "#052822", "#03392C", "#119B6D", "#DEAA6B", "#F1F1EA", "#8AB0AF"):
        assert color in stylesheet


def test_new_dark_theme_stylesheets_load_with_their_primary_colors():
    expected_primary_colors = {
        "onyx": "#D6B46A",
        "halloween": "#E85D24",
        "christmas": "#1E7A4C",
        "cyberpunk": "#00E5FF",
    }

    for theme, color in expected_primary_colors.items():
        assert color in load_styles(theme)


def test_seasonal_sticker_assets_are_present():
    from ui.resources import IMAGES

    assert (IMAGES / "halloween_sticker.svg").is_file()
    assert (IMAGES / "christmas_sticker.svg").is_file()
