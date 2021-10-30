import os

from markdownio import MarkdownIO, block, span


def fixture_path(fixture_name: str):
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    return f'{base_path}/fixtures/{fixture_name}'


def test_markdownio_workflow():
    markdown = MarkdownIO()

    title1 = block.Header1("My test document")
    markdown.add(title1)

    text_p1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
              "Vivamus rutrum consequat " + span.bold("odio") + " et mollis."
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

    title2 = block.Header2("Quote")
    markdown.add(title2)

    block_quote = block.BlockQuote(text="A nice quote!")
    markdown.add(block_quote)

    title3 = block.Header3("Ordered list")
    markdown.add(title3)

    ordered_list = block.OrderedList([
        'Item 1',
        'Item 2',
        'Item 3',
    ])
    markdown.add(ordered_list)

    title4 = block.Header4("Unordered list")
    markdown.add(title4)

    unordered_list = block.UnorderedList([
        'Item 1',
        'Item 2',
        'Item 3',
    ])
    markdown.add(unordered_list)

    title5 = block.Header5("Horizontal rule")
    markdown.add(title5)

    markdown.add(block.HorizontalRule())

    title6 = block.Header6("Code example")
    markdown.add(title6)

    code = block.Code('<p>Test</p>', language='html')
    markdown.add(code)

    with open(fixture_path('example1.md'), 'r') as file:
        assert file.read() == markdown.output()


def test_markdownio_workflow_with_short_syntax():
    markdown = MarkdownIO()

    markdown.h1(text="My test document")
    markdown.p(
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
             "Vivamus rutrum consequat " + span.bold("odio") + " et mollis."
    )
    markdown.p(span.image(path="path/img.jpg", alt="img", title="img"))
    markdown.table(
        columns=3,
        headers=['Col1', 'Col2', 'Col3'],
        rows=[
            ['foo', 'bar', 'foobar'],
            ['oof', 'rab', 2000],
        ]
    )
    markdown.h2(text="Quote")
    markdown.quote(text='A nice quote!')
    markdown.h3(text="Ordered list")
    markdown.ol(items=[
        'Item 1',
        'Item 2',
        'Item 3',
    ])
    markdown.h4(text="Unordered list")
    markdown.ul(items=[
        'Item 1',
        'Item 2',
        'Item 3',
    ])
    markdown.h5("Horizontal rule")
    markdown.hr()
    markdown.h6("Code example")
    markdown.code(text='<p>Test</p>', language='html')

    with open(fixture_path('example1.md'), 'r') as file:
        assert file.read() == markdown.output()


def test_merge_two_documents():
    part_one = MarkdownIO()
    part_one.h1("Part 1")
    part_one.p("This is part 1")
    part_two = MarkdownIO()
    part_two.h1("Part 2")
    part_two.p("This is part 2")

    markdown = part_one + part_two

    with open(fixture_path('example2.md'), 'r') as file:
        assert file.read() == markdown.output()
