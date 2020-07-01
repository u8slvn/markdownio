import os

from markdownio import MarkdownIO, block, span


def test_markdownio_workflow():
    markdown = MarkdownIO()

    title = block.Header1("My test document")
    markdown.add(title)

    text_p1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus " \
              "rutrum consequat " + span.bold("odio") + " et mollis."
    p1 = block.Paragraph(text_p1)
    markdown.add(p1)

    img = block.Paragraph(
        span.image(path="path/img.jpg", alt="img", title="img"))
    markdown.add(img)

    table = block.Table(columns=3)
    table.set_headers(['Col1', 'Col2', 'Col3'])
    table.add_row(['foo', 'bar', 'foobar'])
    table.add_row(['oof', 'rab', 2000])
    markdown.add(table)

    text_p2 = "This is an interesting article: " + span.link(
        path='http://test.io')
    p2 = block.Paragraph(text_p2)
    markdown.add(p2)

    subtitle = block.Header2("Code example")
    markdown.add(subtitle)

    code = block.Code('<p>Test</p>', language='html')
    markdown.add(code)

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'example.md')
    with open(path, 'r') as file:
        assert file.read() == markdown.output()
