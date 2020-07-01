from markdownio import block


def test_table(document):
    elem = block.Table(columns=3)
    elem.set_headers(['one', 'two', 'three'])
    elem.add_row(['Hello', 'World', '!'])
    elem.add_row(['foo', 'bar', 64])
    document.add(elem)

    expected = '| one   | two   | three |\n' \
               '| ----- | ----- | ----- |\n' \
               '| Hello | World | !     |\n' \
               '| foo   | bar   | 64    |\n\n'
    assert expected == document.output()
