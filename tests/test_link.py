from markdownio.elements import link


def test_simple_link():
    md_link = link(path='http://test.com')
    assert '<http://test.com>' == md_link


def test_link_with_title():
    md_link = link(path='http://test.com', title="An example")
    assert '[http://test.com](http://test.com "An example")' == md_link


def test_link_with_text():
    md_link = link(path='http://test.com', text="Example")
    assert '[Example](http://test.com)' == md_link


def test_link_with_text_and_title():
    md_link = link(path='http://test.com', text="Example", title="An example")
    assert '[Example](http://test.com "An example")' == md_link
