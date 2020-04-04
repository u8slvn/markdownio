def test_code_without_language(document):
    text = "<div>\n\t<h1>Title</h1>\n</div>"
    document.code(text=text)

    expected = "```\n<div>\n\t<h1>Title</h1>\n</div>\n```\n\n"
    assert expected == document.output()


def test_code_with_language(document):
    text = "def add(a, b):\n\treturn a + b"
    document.code(text=text, language='python')

    expected = "```python\ndef add(a, b):\n\treturn a + b\n```\n\n"
    assert expected == document.output()
