from markdownio.span import image


def test_simple_image():
    md_image = image(path='./img.jpg')
    assert '![./img.jpg](./img.jpg)' == md_image


def test_image_with_title():
    md_image = image(path='./img.jpg', title='My image')
    assert '![./img.jpg](./img.jpg "My image")' == md_image


def test_image_with_alt():
    md_image = image(path='./img.jpg', alt='Image')
    assert '![Image](./img.jpg)' == md_image


def test_image_with_alt_and_title():
    md_image = image(path='./img.jpg', alt='Image', title='My image')
    assert '![Image](./img.jpg "My image")' == md_image
