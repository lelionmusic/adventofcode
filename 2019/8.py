import sys

image = open("input/input8.txt").read().strip()
WIDTH = 25
HEIGHT = 6
num_layers = len(image) // (WIDTH * HEIGHT)
layers = []
offset = 0
for i in range(num_layers):
    layers.append(image[offset:offset + WIDTH * HEIGHT])
    offset += WIDTH * HEIGHT

counts = [0] * num_layers
for i, layer in enumerate(layers):
    count = 0
    for pixel in layer:
        if pixel == '0':
            count += 1
    counts[i] = count

def find_min(counts):
    min = sys.maxsize
    min_layer = None
    for i, count in enumerate(counts):
        if count < min:
            min = count
            min_layer = i
    return min_layer

def count(layer, digit):
    count = 0
    for pixel in layer:
        if pixel == digit:
            count += 1
    return count

min_zero_layer = find_min(counts)
print("Part 1:", count(layers[min_zero_layer], '1') * count(layers[min_zero_layer], '2'))
