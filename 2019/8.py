import sys
from collections import defaultdict

image = open("input/input8.txt").read().strip()
WIDTH = 25
HEIGHT = 6
LAYER_LENGTH = WIDTH * HEIGHT


def count_pixels(layer) -> dict:
    """ '112220' -> {'1': 2, '2': 3, '0': 1} """
    counts = defaultdict(int)
    for pixel in layer:
        counts[pixel] += 1
    return counts


def find_min(counts: list, val):
    """ Return the dict in counts which contains the leasts val values """
    min = counts[0][val]
    min_layer = counts[0]
    for count in counts:
        if count[val] < min:
            min = count[val]
            min_layer = count
    return min_layer


def construct_image(layers: list) -> str:
    """
    Rules:
    Layer with lower index is in the front
    2 = transparent, 1 = white, 0 = black

    Returns image as a flat string
    Ex.: ['0222', '1122', '2212', '0000'] -> 0110
    """
    final_image = ["2"] * LAYER_LENGTH
    for layer in layers:
        for i, pixel in enumerate(layer):
            if final_image[i] == "2":
                final_image[i] = pixel
    return "".join(final_image)


def print_image(image, width, heigth):
    for i in range(0, len(image), width):
        row = image[i : i + width]
        print("".join(["##" if c == "1" else "  " for c in row]))


# Split image-data evenly into substrings
layers = [image[i : i + LAYER_LENGTH] for i in range(0, len(image), LAYER_LENGTH)]
counts = [count_pixels(layer) for layer in layers]

least_zeroes_layer = find_min(counts, "0")
print("Part 1:", least_zeroes_layer["1"] * least_zeroes_layer["2"])

final_image = construct_image(layers)
print("Part 2:")
print_image(final_image, WIDTH, HEIGHT)
# the image spells FHJUL
