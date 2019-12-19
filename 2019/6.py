from typing import List, Set, Dict

CENTER_OF_MASS = 'COM'

class Planet:
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List['Planet'] = []

    def add_child(self, planet: 'Planet') -> None:
        self.children.append(planet)

    def set_parent(self, parent: 'Planet') -> None:
        self.parent = parent

    def length_to_root(self) -> int:
        if self.name == CENTER_OF_MASS: return 0
        length = 1
        pointer = self
        while pointer.parent.name != CENTER_OF_MASS:
            length += 1
            pointer = pointer.parent
        return length

def print_distance(start: 'Planet', end: 'Planet'):
    visited: Set[str] = set()
    def recurse(current: 'Planet', accum_dist: int):
        if current.name in visited: return
        if current.name == CENTER_OF_MASS: return
        visited.add(current.name)
        if current is end:
            print("Part 2:", accum_dist)
            return
        for planet in current.children + [current.parent]:
            recurse(planet, accum_dist + 1)
    recurse(start, 0)


input_lines = open("input/input6.txt").readlines()
orbit_map = [tuple(line.strip().split(")")) for line in input_lines]

planets: Dict[str, 'Planet'] = {}
for parent, child in orbit_map:
    if parent not in planets:
        planets[parent] = Planet(parent)
    if child not in planets:
        planets[child] = Planet(child)
    planets[parent].add_child(planets[child])
    planets[child].set_parent(planets[parent])

# Part 1: Sum of length of paths from all nodes in tree to root
print("Part 1:", sum([planet.length_to_root() for planet in planets.values()]))

# Part 2
print_distance(planets['YOU'].parent, planets['SAN'].parent)
