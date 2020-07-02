from markdownio import block


def test_blockquote(document):
    quote = "This is a quote.\nA quote on four lines.\r\nHello.\rEnd."
    elem = block.BlockQuote(quote)
    document.add(elem)

    expected = "> This is a quote.\n> A quote on four lines.\n" \
               "> Hello.\n> End.\n\n"
    assert expected == document.output()
