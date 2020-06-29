def italic(text: str) -> str:
    return f'_{text}_'


def bold(text: str) -> str:
    return f'**{text}**'


def strikethrough(text: str) -> str:
    return f'~~{text}~~'


def code(text: str) -> str:
    return f'`{text}`'


def link(path: str, text: str = None, title: str = None) -> str:
    if not any([text, title]):
        return f'<{path}>'
    text = text or path
    title = f' "{title}"' if title else ''
    return f'[{text}]({path}{title})'


def image(path: str, alt: str = None, title: str = None) -> str:
    alt = alt or path
    title = f' "{title}"' if title else ''
    return f'![{alt}]({path}{title})'
