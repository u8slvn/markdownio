# MarkdownIO
[![Pypi Version](https://img.shields.io/pypi/v/markdownio.svg)](https://pypi.org/project/markdownio/)
[![Python Version](https://img.shields.io/pypi/pyversions/markdownio)](https://pypi.org/project/markdownio/)
[![Build Status](https://travis-ci.org/u8slvn/markdownio.svg?branch=master)](https://travis-ci.org/u8slvn/markdownio)
[![Coverage Status](https://coveralls.io/repos/github/u8slvn/markdownio/badge.svg?branch=master)](https://coveralls.io/github/u8slvn/markdownio?branch=master)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Project license](https://img.shields.io/pypi/l/markdownio)](https://pypi.org/project/markdownio/)

Python tool to write Markdown as code easily.

## Installation

```sh
$ pip install markdownio
```

## Usage

```python
from markdownio import MarkdownIO, block, span


markdown = MarkdownIO()

title = block.Header1("My test document")
markdown.add(title)

text_p1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus " \
          "rutrum consequat " + span.bold("odio") + " et mollis."
p1 = block.Paragraph(text_p1)
markdown.add(p1)

img = block.Paragraph(span.image(path="path/img.jpg", alt="img", title="img"))
markdown.add(img)

table = block.Table(columns=3)
table.set_headers(['Col1', 'Col2', 'Col3'])
table.add_row(['foo', 'bar', 'foobar'])
table.add_row(['oof', 'rab', 2000])
markdown.add(table)

text_p2 = "This is an interesting article: " + span.link(path='http://test.io')
p2 = block.Paragraph(text_p2)
markdown.add(p2)

subtitle = block.Header2("Code example")
markdown.add(subtitle)

code = block.Code('<p>Test</p>', language='html')
markdown.add(code)

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
