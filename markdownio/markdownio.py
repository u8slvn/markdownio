from io import StringIO
from typing import List

from markdownio.elements import SubList


class MarkdownIO:
    def __init__(self, newline: str = '\n'):
        self._newline = newline
        self._buffer = StringIO(newline=newline)

    def _header(self, level: int, text: str):
        if level not in range(1, 7):
            raise ValueError("Markdown header level must be between 1 to 6.")

        print(f"{'#' * level} {text}", file=self._buffer)

    def header1(self, text: str):
        self._header(level=1, text=text)

    def header2(self, text: str):
        self._header(level=2, text=text)

    def header3(self, text: str):
        self._header(level=3, text=text)

    def header4(self, text: str):
        self._header(level=4, text=text)

    def header5(self, text: str):
        self._header(level=5, text=text)

    def header6(self, text: str):
        self._header(level=6, text=text)

    def _list(self, items: List, ordered: bool, _level: int = None):
        level = _level or 0
        for n, item in enumerate(items, 1):
            if isinstance(item, SubList):
                sub_level = level + 1
                self._list(item.items, item.ordered, sub_level)
                continue

            prefix = f"{n}." if ordered else '*'
            prefix = f"{'  ' * level}{prefix}"
            print(f"{prefix} {item}", file=self._buffer)
        if level == 0:
            self.newline()

    def ordered_list(self, items: List):
        self._list(items=items, ordered=True)

    def unordered_list(self, items: List):
        self._list(items=items, ordered=False)

    def code(self, text:str, language:str = ''):
        print(f"```{language}\n{text}\n```", file=self._buffer)
        self.newline()

    def horizontal_rule(self):
        print('---', file=self._buffer)
        self.newline()

    def blockquote(self, text: str):
        lines = text.split(self._newline)
        for line in lines:
            print(f"> {line}", file=self._buffer)
        self.newline()

    def output(self):
        return self._buffer.getvalue()

    def newline(self):
        print('', file=self._buffer)

    def close(self):
        self._buffer.close()
