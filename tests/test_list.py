from markdownio.elements import OrderedSubList, UnorderedSubList


def test_write_ordered_list(document):
    document.ordered_list(['First item', 'Second item', 'Last item'])

    expected = '1. First item\n2. Second item\n3. Last item\n\n'
    assert expected == document.output()


def test_write_unordered_list(document):
    document.unordered_list(['First item', 'Second item', 'Last item'])

    expected = '* First item\n* Second item\n* Last item\n\n'
    assert expected == document.output()


def test_write_list_with_sub_lists(document):
    document.unordered_list([
            'First item',
            'Second item',
            OrderedSubList([
                'Sub-list item',
                'Another sub-list item',
            ]),
            'Third item',
            UnorderedSubList([
                'Sub-list item',
                'Another sub-list item',
            ]),
            'Last item',
        ])

    expected = '* First item\n* Second item\n  1. Sub-list item\n  ' \
               '2. Another sub-list item\n* Third item\n  ' \
               '* Sub-list item\n  * Another sub-list item\n* Last item\n\n'
    assert expected == document.output()
