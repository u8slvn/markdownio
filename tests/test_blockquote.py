def test_blockquote(document):
    document.blockquote("This is a quote.\nA quote on two lines.")

    expected = "> This is a quote.\n> A quote on two lines.\n\n"
    assert expected == document.output()
