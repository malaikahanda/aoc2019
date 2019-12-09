from collections import Counter

HEIGHT = 6
WIDTH = 25
LAYER_LEN = HEIGHT * WIDTH
BLACK = "0"
WHITE = "1"
TRANSP = "2"

def stack_layers(image):
    
    stacked = {}

    for i in range(0, len(image), LAYER_LEN):
        layer = image[i : i + LAYER_LEN]
        
        for i, pixel in enumerate(layer):
            if i in stacked:
                stacked[i].append(pixel)
            else:
                stacked[i] = [pixel]

    return stacked


def get_visible_pixel(stack):
    for p in stack:
        if p != TRANSP:
            return p


def compress_image(image):
    out = []
    for i in range(len(image)):
        pixels = image[i]
        visible = get_visible_pixel(pixels)
        out.append(visible)
    return out


def print_picture(picture):
    for i in range(0, len(picture), WIDTH):
        row = picture[i : i + WIDTH]
        out = []
        for e in row:
            if e == BLACK:
                out.append(" ")
            else:
                out.append("#")
        print("".join(out))
    return


with open("input.txt") as f:
    image = list(f.read().strip())
    stacked = stack_layers(image)
    picture = compress_image(stacked)
    print_picture(picture)



