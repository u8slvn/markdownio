from abc import ABC, abstractmethod
from io import StringIO
from typing import List as _List

NEWLINE = '\n'


class Block(ABC):
    _newline = NEWLINE

    @abstractmethod
    def render(self, buffer: StringIO):
        pass


class Header(Block):
    def __init__(self, level: int, text: str):
        if level not in range(1, 7):
            raise ValueError("Markdown header level must be between 1 to 6.")
        self.level = level
        self.text = text

    def render(self, buffer: StringIO):
        print(f"{'#' * self.level} {self.text}", file=buffer)


class Header1(Header):
    def __init__(self, text: str):
        super().__init__(level=1, text=text)


class Header2(Header):
    def __init__(self, text: str):
        super().__init__(level=2, text=text)


class Header3(Header):
    def __init__(self, text: str):
        super().__init__(level=3, text=text)


class Header4(Header):
    def __init__(self, text: str):
        super().__init__(level=4, text=text)


class Header5(Header):
    def __init__(self, text: str):
        super().__init__(level=5, text=text)


class Header6(Header):
    def __init__(self, text: str):
        super().__init__(level=6, text=text)


class List(Block):
    def __init__(self, items: _List, ordered: bool):
        self.items = items
        self.ordered = ordered

    def render(self, buffer: StringIO, _tab: int = 0):
        for n, item in enumerate(self.items, 1):
            if isinstance(item, List):
                sub_tab = _tab + 1
                item.render(buffer=buffer, _tab=sub_tab)
                continue

            prefix = f"{n}." if self.ordered else '*'
            prefix = f"{'  ' * _tab}{prefix}"
            print(f"{prefix} {item}", file=buffer)


class OrderedList(List):
    def __init__(self, items: _List):
        super().__init__(items=items, ordered=True)


class UnOrderedList(List):
    def __init__(self, items: _List):
        super().__init__(items=items, ordered=False)


class BlockQuote(Block):
    def __init__(self, text: str):
        self.text = text

    def render(self, buffer: StringIO):
        lines = self.text.split(self._newline)
        for line in lines:
            print(f"> {line}", file=buffer)


class HorizontalRule(Block):
    def render(self, buffer: StringIO):
        print('---', file=buffer)


class Code(Block):
    def __init__(self, text: str, language: str = ''):
        self.text = text
        self.language = language

    def render(self, buffer: StringIO):
        print(f'```{self.language}\n{self.text}\n```', file=buffer)
