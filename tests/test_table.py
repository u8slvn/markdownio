import pytest

from markdownio import block


def test_table(document):
    elem = block.Table(columns=3)
    elem.set_headers(['one', 'two', 'three'])
    elem.add_row(['Hello', 'World', '!'])
    elem.add_row(['foo', 'bar', 64])
    elem.add_rows([
        ['multiple', 'rows', 'test 1'],
        ['multiple', 'rows', 'test 2'],
    ])
    document.add(elem)

    expected = '| one      | two   | three  |\n' \
               '| -------- | ----- | ------ |\n' \
               '| Hello    | World | !      |\n' \
               '| foo      | bar   | 64     |\n' \
               '| multiple | rows  | test 1 |\n' \
               '| multiple | rows  | test 2 |\n'
    assert expected == document.output()


def test_row_must_respect_nb_columns():
    elem = block.Table(columns=3)
    with pytest.raises(ValueError):
        elem.add_row(['Hello', 'World', 'Wrong', '!'])


def test_header_must_respect_nb_columns():
    elem = block.Table(columns=3)
    with pytest.raises(ValueError):
        elem.set_headers(['one', 'two', 'three', 'wrong'])
