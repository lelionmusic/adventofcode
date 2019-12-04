from operator import add

with open("input/input3.txt") as data:
    wire1 = data.readline().split(',')
    wire2 = data.readline().split(',')

def plot_path(wire):
    position = [0, 0]
    path = []

    for movement in wire:
        direction = movement[0]
        length = int(movement[1:])
        for i in range(1, length + 1):
            if direction == 'U':
                path.append((position[0], position[1] + i))
            elif direction == 'R':
                path.append((position[0] + i, position[1]))
            elif direction == 'D':
                path.append((position[0], position[1] - i))
            elif direction == 'L':
                path.append((position[0] - i, position[1]))
        position = path[-1]
    return path

wire1_path = plot_path(wire1)
wire2_path = plot_path(wire2)
intersections = set(wire1_path).intersection(set(wire2_path))

# print("Part 1:", min(map(sum, map(lambda x: map(abs, x), intersections))))
print("Part 1:", min([abs(x[0]) + abs(x[1]) for x in intersections]))

def find_steps(path):
    return [i+1 for intersection in intersections for i, pos in enumerate(path) if pos == intersection]

summed_steps = list(map(add, find_steps(wire1_path), find_steps(wire2_path)))
print("Part 2:", min(summed_steps))
