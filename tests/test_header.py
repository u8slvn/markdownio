def test_write_header1(document):
    document.header1("Main title")
    assert "# Main title\n" == document.output()


def test_write_header2(document):
    document.header2("Super big title")
    assert "## Super big title\n" == document.output()


def test_write_header3(document):
    document.header3("Big title")
    assert "### Big title\n" == document.output()


def test_write_header4(document):
    document.header4("Medium title")
    assert "#### Medium title\n" == document.output()


def test_write_header5(document):
    document.header5("Small title")
    assert "##### Small title\n" == document.output()


def test_write_header6(document):
    document.header6("Super small title")
    assert "###### Super small title\n" == document.output()
