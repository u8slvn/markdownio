import pytest

from markdownio import MarkdownIO


@pytest.fixture(scope='function')
def document():
    document = MarkdownIO()
    return document
