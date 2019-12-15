import sys
from collections import defaultdict

image = open("input/input8.txt").read().strip()
WIDTH = 25
HEIGHT = 6
layer_length = WIDTH * HEIGHT


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


# Split image-data evenly into substrings
layers = [image[i : i + layer_length :] for i in range(0, len(image), layer_length)]
counts = [count_pixels(layer) for layer in layers]

least_zeroes_layer = find_min(counts, "0")
print("Part 1:", least_zeroes_layer["1"] * least_zeroes_layer["2"])
