from markdownio import block, span


def test_code_without_language(document):
    text = "<div>\n\t<h1>Title</h1>\n</div>"
    elem = block.Code(text=text)
    document.add(elem)

    expected = "```\n<div>\n\t<h1>Title</h1>\n</div>\n```\n\n"
    assert expected == document.output()


def test_code_with_language(document):
    text = "def add(a, b):\n\treturn a + b"
    elem = block.Code(text=text, language='python')
    document.add(elem)

    expected = "```python\ndef add(a, b):\n\treturn a + b\n```\n\n"
    assert expected == document.output()


def test_span_code(document):
    text = "This is " + span.code("code") + "."
    assert "This is `code`." == text
