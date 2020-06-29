from markdownio import span


def test_simple_link():
    md_link = span.link(path='http://test.com')
    assert '<http://test.com>' == md_link


def test_link_with_title():
    md_link = span.link(path='http://test.com', title="Test")
    assert '[http://test.com](http://test.com "Test")' == md_link


def test_link_with_text():
    md_link = span.link(path='http://test.com', text="Test")
    assert '[Test](http://test.com)' == md_link


def test_link_with_text_and_title():
    md_link = span.link(path='http://test.com', text="Test", title="Test")
    assert '[Test](http://test.com "Test")' == md_link
