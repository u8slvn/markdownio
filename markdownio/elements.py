from abc import ABC
from typing import List


class SubList(ABC):
    def __init__(self, ordered: bool, items: List):
        self.ordered = ordered
        self.items = items


class OrderedSubList(SubList):
    def __init__(self, items: List):
        super().__init__(ordered=True, items=items)


class UnorderedSubList(SubList):
    def __init__(self, items: List):
        super().__init__(ordered=False, items=items)


def italic(text: str) -> str:
    return f"_{text}_"


def bold(text: str) -> str:
    return f"**{text}**"


def strikethrough(text: str) -> str:
    return f"~~{text}~~"


def link(path: str, text: str = None, title: str = None) -> str:
    if not any([text, title]):
        return f"<{path}>"
    text = text or path
    title = f" \"{title}\"" if title else ''
    return f"[{text}]({path}{title})"


def image(path: str, alt: str = None, title: str = None) -> str:
    alt = alt or path
    title = f" \"{title}\"" if title else ''
    return f"![{alt}]({path}{title})"
