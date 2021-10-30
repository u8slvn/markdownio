from abc import ABC, abstractmethod
from collections import defaultdict
from contextlib import suppress
from enum import Enum, auto
from io import StringIO
from itertools import starmap
from typing import List

TABULATION = " " * 4


class Block(ABC):
    _tabulation = TABULATION

    @abstractmethod
    def render(self, buffer: StringIO):
        raise NotImplementedError


class Paragraph(Block):
    def __init__(self, text: str):
        self.text = text

    def render(self, buffer: StringIO):
        print(self.text, file=buffer)


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


class BlockList(Block):
    def __init__(self, items: List, ordered: bool):
        self.items = items
        self.ordered = ordered

    def render(self, buffer: StringIO, level: int = 0):
        for n, item in enumerate(self.items, 1):
            if isinstance(item, List):
                item = BlockList(items=item, ordered=self.ordered)
            if isinstance(item, BlockList):
                sub_tab = level + 1
                item.render(buffer=buffer, level=sub_tab)
                continue

            prefix = f"{n}." if self.ordered else "*"
            prefix = f"{self._tabulation * level}{prefix}"
            print(f"{prefix} {item}", file=buffer)


class OrderedList(BlockList):
    def __init__(self, items: List):
        super().__init__(items=items, ordered=True)


class UnorderedList(BlockList):
    def __init__(self, items: List):
        super().__init__(items=items, ordered=False)


class BlockQuote(Block):
    def __init__(self, text: str):
        self.text = text

    def render(self, buffer: StringIO):
        lines = self.text.splitlines()
        for line in lines:
            print(f"> {line}", file=buffer)


class HorizontalRule(Block):
    def render(self, buffer: StringIO):
        print("---", file=buffer)


class Code(Block):
    def __init__(self, text: str, language: str = ""):
        self.text = text
        self.language = language

    def render(self, buffer: StringIO):
        print(f"```{self.language}\n{self.text}\n```", file=buffer)


class _Alignment(Enum):
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()


class TableHeader:
    def __init__(self, text, alignment: _Alignment):
        self.text = text
        self.alignment = alignment

    @classmethod
    def left(cls, text):
        return cls(text=text, alignment=_Alignment.LEFT)

    @classmethod
    def right(cls, text):
        return cls(text=text, alignment=_Alignment.RIGHT)

    @classmethod
    def center(cls, text):
        return cls(text=text, alignment=_Alignment.CENTER)


class Table(Block):
    def __init__(self, columns: int):
        self.columns = columns
        self.headers = []
        self._alignments = []
        self._rows = []
        self.max_col_widths = defaultdict(int)

    @property
    def rows(self):
        return self.headers + self._rows

    def _check_row_length(self, row: List):
        if len(row) != self.columns:
            raise ValueError(
                "A new row must be the same size as the number " "of columns."
            )

    def _update_max_col_widths(self, row_index: int = None):
        if not isinstance(row_index, int):
            row_index = len(self.rows) - 1  # Last index by default.
        for index, value in enumerate(self.rows[row_index]):
            value = str(value)
            if self.max_col_widths[index] < len(value):
                self.max_col_widths[index] = len(value)

    def set_headers(self, headers: List):
        self._check_row_length(row=headers)
        for index, header in enumerate(headers):
            if isinstance(header, TableHeader):
                headers[index] = header.text
                self._alignments.append(header.alignment)
                continue
            self._alignments.append(_Alignment.LEFT)  # Left by default
        self.headers.insert(0, headers)
        self._update_max_col_widths(row_index=0)

    def add_row(self, row: List):
        self._check_row_length(row=row)
        self._rows.append(row)
        self._update_max_col_widths()

    def add_rows(self, rows: List[List]):
        for row in rows:
            self.add_row(row=row)

    @staticmethod
    def _build_header_rule(max_col_width: int, alignment: _Alignment):
        max_col_width = max_col_width if max_col_width > 3 else 3
        return {
            _Alignment.RIGHT: f'{"-" * (max_col_width - 1)}:',
            _Alignment.CENTER: f':{"-" * (max_col_width - 2)}:',
        }.get(
            alignment, f'{"-" * max_col_width}'
        )  # Return left by default.

    def _generate_header(self):
        header_rules = zip(self.max_col_widths.values(), self._alignments)
        header_rules = list(starmap(self._build_header_rule, header_rules))
        with suppress(IndexError):
            del self.headers[1]
        self.headers.insert(1, header_rules)
        self._update_max_col_widths(row_index=1)

    def _render_row(self, row: List):
        for index, value in enumerate(row):
            value = str(value)
            width_diff = self.max_col_widths[index] - len(value)
            if width_diff > 0:
                row[index] = f'{row[index]}{" " * width_diff}'
        return f'| {" | ".join(row)} |'

    def render(self, buffer: StringIO):
        self._generate_header()
        for row in self.rows:
            print(self._render_row(row), file=buffer)
