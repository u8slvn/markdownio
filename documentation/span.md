[← Back to README](../README.md)

## Span

Spam elements are inline markdown blocks like image, bold text, or hypertext link. A span element is basically a string
so it must mandatorily be placed inside a [block element](./block.md).

```python
from markdownio import MarkdownIO, span

document = MarkdownIO()
document.p(span.link(path="http://test.com"))
print(document.output())
```

output:

```markdown
<http://test.com>
```

### - Link

```python
document.p(span.link(path="http://test.com"))
document.p(span.link(path="http://test.com", text="hello"))
document.p(span.link(path="http://test.com", title="hello"))
document.p(span.link(path="http://test.com", text="hello", title="hello"))
```

```markdown
<http://test.com>

[hello](http://test.com)

[http://test.com](http://test.com "hello")

[hello](http://test.com "hello")
```

### - Emphasis

```python
document.p("Hello " + span.bold(text="world") + "!")
document.p("Hello " + span.italic(text="world") + "!")
document.p("Hello " + span.strikethrough(text="world") + "!")
document.p("Hello " + span.bold(text=span.italic(text="world")) + "!")
```

```markdown
Hello **world**!

Hello _world_!

Hello ~~world~~!

Hello **_world_**!
```

### Image

```python
document.p(span.image(path="http://test.com/img.jpg"))
document.p(span.link(path="http://test.com/img.jpg", alt="img"))
document.p(span.link(path="http://test.com/img.jpg"), title="img")
document.p(span.link(path="http://test.com/img.jpg"), alt="img", title="img")
```

```markdown
![http://test.com/img.jpg](http://test.com/img.jpg)
![http://test.com/img.jpg](http://test.com/img.jpg "img")
![img](http://test.com/img.jpg)
![img](http://test.com/img.jpg "img")
```

[← Back to README](../README.md)