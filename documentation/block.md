[← Back to README](../README.md)

## Block

Block elements are basic block structure of markdown document. You can build them independently and add them to a **
MarkdownIO** document or you can also use **MarkdownIO** short syntax. Then just call `output` method to build the
markdown document.

```python
from markdownio import MarkdownIO, block

document = MarkdownIO()

h1 = block.Header1(text="Hello")
document.add(h1)

# Short syntax
document.p(text="Hello.")

print(document.output())
```

output:

```markdown
# Hello

Hello.
```

### - Paragraph

```python
document.p(text="This is a paragraph.")
```

```markdown
This is a paragraph.
```

### - Headers

```python
document.h1(text="H1 header")
document.h2(text="H2 header")
document.h3(text="H3 header")
document.h4(text="H4 header")
document.h5(text="H5 header")
document.h6(text="H6 header")
```

```markdown
# H1 header

## H2 header

### H3 header

#### H4 header

##### H5 header

###### H6 header
```

### - List

```python
document.ul(items=["foo", "bar"])
document.ol(items=["foo", "bar"])
document.ul(items=["foo", "bar", ["oof", "rab"], "foobar"])
```

```markdown
* foo
* bar

1. foo
2. bar

* foo
* bar
    * oof
    * rab
* foobar
```

Mixed list with `OrderedList` or `UnorderedList`:

```python
from markdownio.block import OrderedList

document.ul(items=["foo", "bar", OrderedList(items=["oof", "rab"], "foobar")])
```

```markdown
* foo
* bar
    1. oof
    2. rab
* foobar
```

### - Block quote

```python
document.quote(text="This is a quote.")
```

```markdown
> This is a quote.
```

### - Horizontal rule

```python
document.hr()
```

```markdown
---
```

### - Code

```python
document.code(text="<p>Html here!<\p>", language="html")
```

~~~markdown
```html
<p>Html here!<\p>
```
~~~

### - Table

Column alignments: `TableHeader.center`, `TableHeader.left` and `TableHeader.right`

```python
from markdownio.block import TableHeader

document.table(
    columns=3,
    headers=['Col1', 'Col2', TableHeader.center('Col3')],
    rows=[
        ['foo', 'bar', 'foobar'],
        ['oof', 'rab', 2000],
    ]
)
```

```markdown
| Col1 | Col2 | Col3   |
| ---- | ---- | :----: |
| foo  | bar  | foobar |
| oof  | rab  | 2000   |
```

[← Back to README](../README.md)