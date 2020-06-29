from markdownio.span import bold, italic, strikethrough


def test_bold():
    text = "This is " + bold("bold") + "."
    assert "This is **bold**." == text


def test_italic():
    text = "This is " + italic("italic") + "."
    assert "This is _italic_." == text


def test_strikethrough():
    text = "This is " + strikethrough("strikethrough") + "."
    assert "This is ~~strikethrough~~." == text


def test_combined_emphasis():
    text = "This is " + bold("bold with " + italic("italic")) + "."
    assert "This is **bold with _italic_**." == text
