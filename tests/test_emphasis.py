from markdownio import span


def test_bold():
    text = "This is " + span.bold("bold") + "."
    assert "This is **bold**." == text


def test_italic():
    text = "This is " + span.italic("italic") + "."
    assert "This is _italic_." == text


def test_strikethrough():
    text = "This is " + span.strikethrough("strikethrough") + "."
    assert "This is ~~strikethrough~~." == text


def test_combined_emphasis():
    text = "This is " + span.bold("bold with " + span.italic("italic")) + "."
    assert "This is **bold with _italic_**." == text
