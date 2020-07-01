from markdownio import block


def test_blockquote(document):
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n" \
           "Vivamus rutrum consequat odio et mollis."
    elem = block.Paragraph(text)
    document.add(elem)

    expected = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n" \
               "Vivamus rutrum consequat odio et mollis.\n\n"
    assert expected == document.output()
