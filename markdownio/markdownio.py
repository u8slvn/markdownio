from io import StringIO

from markdownio.block import Block


class MarkdownIO:
    def __init__(self):
        self._elements = []

    def add(self, element: Block):
        self._elements.append(element)

    def output(self):
        buffer = StringIO()
        for element in self._elements:
            element.render(buffer=buffer)
            print('', file=buffer)  # new line
        markdown = buffer.getvalue()
        buffer.close()
        return markdown
