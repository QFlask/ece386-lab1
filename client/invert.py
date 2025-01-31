from PIL import Image, ImageChops

""" For those that unfortunately draw black on white digits..."""


def invert_image(path):
    image = Image.open(path)
    inverted_image = ImageChops.invert(image)
    return inverted_image


for i in range(10):
    path = f"./img/{i}.png"
    inverted_image = invert_image(path)
    inverted_image.save(path)
