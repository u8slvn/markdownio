# MarkdownIO
[![Pypi Version](https://img.shields.io/pypi/v/markdownio.svg)](https://pypi.org/project/markdownio/)
[![Python Version](https://img.shields.io/pypi/pyversions/markdownio)](https://pypi.org/project/markdownio/)
[![CI](https://github.com/u8slvn/markdownio/actions/workflows/ci.yml/badge.svg)](https://github.com/u8slvn/markdownio/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/u8slvn/markdownio/badge.svg?branch=master)](https://coveralls.io/github/u8slvn/markdownio?branch=master)
[![Project license](https://img.shields.io/pypi/l/markdownio)](https://pypi.org/project/markdownio/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python tool to write Markdown as code easily.

## Installation

```sh
$ pip install markdownio
```

## Usage

```python
from markdownio import MarkdownIO, span


markdown = MarkdownIO()

markdown.h1("My test document")
markdown.p(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
         "Vivamus rutrum consequat " + span.bold("odio") + " et mollis."
)
markdown.p(span.image(path="path/img.jpg", alt="img", title="img"))
markdown.table(
    columns=3,
    headers=['Col1', 'Col2', 'Col3'],
    rows=[
        ['foo', 'bar', 'foobar'],
        ['oof', 'rab', 2000],
    ]
)
markdown.p(
    text="This is an interesting article: " + span.link(path='http://test.io')
)
markdown.h2("Code example")
markdown.code(text='<p>Test</p>', language='html')

print(markdown.output())
```

output:

~~~markdown
# My test document

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus rutrum consequat **odio** et mollis.

![img](path/img.jpg "img")

| Col1 | Col2 | Col3   |
| ---- | ---- | ------ |
| foo  | bar  | foobar |
| oof  | rab  | 2000   |

This is an interesting article: <http://test.io>

## Code example

```html
<p>Test</p>
```
~~~
