from markdownio import block


def test_write_ordered_list(document):
    elem = block.OrderedList(['First item', 'Second item', 'Last item'])
    document.add(elem)

    expected = '1. First item\n2. Second item\n3. Last item\n\n'
    assert expected == document.output()


def test_write_unordered_list(document):
    elem = block.UnorderedList(['First item', 'Second item', 'Last item'])
    document.add(elem)

    expected = '* First item\n* Second item\n* Last item\n\n'
    assert expected == document.output()


def test_write_list_with_sub_lists(document):
    elem = block.List(
        [
            'First item',
            'Second item',
            block.OrderedList([
                'Sub-list item',
                'Another sub-list item',
            ]),
            'Third item',
            block.UnorderedList([
                'Sub-list item',
                'Another sub-list item',
            ]),
            'Last item'
        ],
        ordered=False
    )
    document.add(elem)

    expected = '* First item\n* Second item\n' \
               '    1. Sub-list item\n    2. Another sub-list item\n' \
               '* Third item\n' \
               '    * Sub-list item\n    * Another sub-list item\n' \
               '* Last item\n\n'
    assert expected == document.output()
