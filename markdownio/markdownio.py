from io import StringIO

from markdownio.block import (
    Block,
    Paragraph,
    Header1,
    Header2,
    Header3,
    Header4,
    Header5,
    Header6,
    OrderedList,
    UnorderedList,
    BlockQuote,
    Table,
    Code,
    HorizontalRule,
)
from typing import List


class MarkdownIO:
    def __init__(self):
        self._elements = []

    def add(self, element: Block):
        self._elements.append(element)

    def output(self) -> str:
        buffer = StringIO()
        for element in self._elements:
            element.render(buffer=buffer)
            print("", file=buffer)  # new line
        markdown = buffer.getvalue()
        buffer.close()
        return markdown

    def p(self, text: str):
        self.add(Paragraph(text=text))

    def h1(self, text: str):
        self.add(Header1(text=text))

    def h2(self, text: str):
        self.add(Header2(text=text))

    def h3(self, text: str):
        self.add(Header3(text=text))

    def h4(self, text: str):
        self.add(Header4(text=text))

    def h5(self, text: str):
        self.add(Header5(text=text))

    def h6(self, text: str):
        self.add(Header6(text=text))

    def ordered_list(self, items: List):
        self.add(OrderedList(items=items))

    def unordered_list(self, items: List):
        self.add(UnorderedList(items=items))

    def quote(self, text: str):
        self.add(BlockQuote(text=text))

    def hr(self):
        self.add(HorizontalRule())

    def code(self, text: str, language: str = ""):
        self.add(Code(text=text, language=language))

    def table(self, columns: int, headers: List, rows: List):
        _table = Table(columns=columns)
        _table.set_headers(headers=headers)
        _table.add_rows(rows=rows)
        self.add(_table)
