from markdownio import block


def test_blockquote(document):
    elem = block.BlockQuote("This is a quote.\nA quote on two lines.")
    document.add(elem)

    expected = "> This is a quote.\n> A quote on two lines.\n\n"
    assert expected == document.output()
