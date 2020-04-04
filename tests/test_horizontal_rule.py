def test_linebreak(document):
    document.horizontal_rule()
    assert "---\n\n" == document.output()
