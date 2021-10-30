import pytest

from markdownio import block


def test_table(document):
    elem = block.Table(columns=4)
    elem.set_headers([
        'one',
        block.TableHeader.right('two'),
        block.TableHeader.center('three'),
        block.TableHeader.left('four'),
    ])
    elem.add_row(['Hello', 'World', '!', '!'])
    elem.add_row(['foo', 'bar', 'oof', 'rab'])
    elem.add_rows([
        ['multiple', 'rows', 'test', 1],
        ['multiple', 'rows', 'test', 2],
    ])
    document.add(elem)

    expected = '| one      | two   | three | four |\n' \
               '| -------- | ----: | :---: | ---- |\n' \
               '| Hello    | World | !     | !    |\n' \
               '| foo      | bar   | oof   | rab  |\n' \
               '| multiple | rows  | test  | 1    |\n' \
               '| multiple | rows  | test  | 2    |\n'
    assert expected == document.output()


def test_row_must_respect_nb_columns():
    elem = block.Table(columns=3)
    with pytest.raises(ValueError):
        elem.add_row(['Hello', 'World', 'Wrong', '!'])


def test_header_must_respect_nb_columns():
    elem = block.Table(columns=3)
    with pytest.raises(ValueError):
        elem.set_headers(['one', 'two', 'three', 'wrong'])
