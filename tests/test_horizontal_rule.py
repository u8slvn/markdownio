from markdownio import block


def test_linebreak(document):
    elem = block.HorizontalRule()
    document.add(elem)
    assert "---\n\n" == document.output()
