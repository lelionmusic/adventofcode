from functools import reduce
terrain = [line.strip() for line in open("03-input.txt").readlines()]

PATTERN_WIDTH = len(terrain[0])

def check_slope(right, down):
    current_x_position = right
    number_of_trees = 0
    for horizontal_line in terrain[down::down]:
        if horizontal_line[current_x_position] == '#':
            number_of_trees += 1
        current_x_position += right
        current_x_position = current_x_position % PATTERN_WIDTH
    return number_of_trees

print("Part 1")
print(check_slope(3, 1))

print("Part 2")
part_2_answer = reduce((lambda x, y: x * y), [check_slope(el[0], el[1]) for el in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])
print(part_2_answer)
