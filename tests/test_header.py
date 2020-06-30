import pytest

from markdownio import block


def test_write_header1(document):
    elem = block.Header1("Main title")
    document.add(elem)
    assert "# Main title\n\n" == document.output()


def test_write_header2(document):
    elem = block.Header2("Super big title")
    document.add(elem)
    assert "## Super big title\n\n" == document.output()


def test_write_header3(document):
    elem = block.Header3("Big title")
    document.add(elem)
    assert "### Big title\n\n" == document.output()


def test_write_header4(document):
    elem = block.Header4("Medium title")
    document.add(elem)
    assert "#### Medium title\n\n" == document.output()


def test_write_header5(document):
    elem = block.Header5("Small title")
    document.add(elem)
    assert "##### Small title\n\n" == document.output()


def test_write_header6(document):
    elem = block.Header6("Super small title")
    document.add(elem)
    assert "###### Super small title\n\n" == document.output()


def test_wrong_header_level(document):
    with pytest.raises(ValueError):
        _ = block.Header(level=7, text="Wrong header")
