from collections import defaultdict
from math import sqrt, atan2

def draw_map(asteroid_map):
    """ Pretty print the asteroid map """
    for y, row in enumerate(asteroid_map):
        for x, column_element in enumerate(row):
            print(column_element + " ", end="")
        print()

# def vector_parallell(a, b):
#     a_magnitude = vector_magnitude(a)
#     a_unit_vec = (a[0] / a_magnitude, a[1] / a_magnitude)
#     b_magnitude = vector_magnitude(b)
#     b_unit_vec = (b[0] / b_magnitude, b[1] / b_magnitude)
#     return round(a_unit_vec[0], 5) == round(b_unit_vec[0], 5) \
#         and round(a_unit_vec[1], 5) == round(b_unit_vec[1], 5)


# def obstructed(pos, asteroid) -> bool:
#     """ Return true if there is at least 1 other asteroid between pos and asteroid"""
#     # if there exists a vector between pos and obstacle equal to
#     # the vector between pos and asteroid, it is obstructed
#     vector1 = (asteroid[0] - pos[0], asteroid[1] - pos[1])
#     for obstacle in asteroids:
#         if obstacle == pos or obstacle == asteroid:
#             continue
#         vector2 = (obstacle[0] - pos[0], obstacle[1] - pos[1])
#         if vector_parallell(vector1, vector2) \
#            or vector_magnitude(vector2) < vector_magnitude(vector1):
#                 return True
#     return False

""" First implementation, very inefficient at O(n^3) or something. Almost 4 mins to run"""
# def count_visible(asteroids, pos):
#     visible = 0
#     for asteroid in asteroids:
#         if pos == asteroid or obstructed(pos, asteroid):
#             continue
#         visible += 1
#     return visible


def vector_magnitude(a):
    return sqrt(a[0] ** 2 + a[1] ** 2)

def count_visible_optimized(asteroids, pos):
    vectors = set()
    for asteroid in asteroids:
        if pos == asteroid:
            continue
        vector = (asteroid[0] - pos[0], asteroid[1] - pos[1])
        magnitude = vector_magnitude(vector)
        unit_vector = (round(vector[0] / magnitude, 5), round(vector[1] / magnitude, 5))
        vectors.add(unit_vector)
    return len(vectors)


with open("input/input10.txt") as input_file:
    asteroid_map = [line.strip() for line in input_file.readlines()]

asteroids = [
    (x, y)
    for y, row in enumerate(asteroid_map)
    for x, pos in enumerate(row)
    if pos == "#"
]

""" Second implementation, improved to O(n^2). Around 0.5s to run"""
# visible_asteroids = defaultdict(int)
# for pos in asteroids:
#     visible_asteroids[pos] = count_visible_optimized(asteroids, pos)
# max_visible = max(visible_asteroids.values())
# print("Part 1:", max_visible)

"""
Third implementation, optimized by calculating angles instead of unit vectors.
Runs at around 120ms
The answer is the max number of unique angles between an asteroid and all other asteroids
One liner for fun
"""
print("Part 1:", max([len(set([atan2(pos[0] - asteroid[0], pos[1] - asteroid[1]) for asteroid in asteroids])) for pos in asteroids]))
