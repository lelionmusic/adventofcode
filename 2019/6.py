from __future__ import annotations
from typing import List, NewType

CENTER_OF_MASS = 'COM'

class Planet:
    def __init__(self, name: str, parent: Planet = None) -> None:
        self.name = name
        self.parent = parent
        self.children = []

    def __repr__(self) -> str:
        return self.name

    def add_child(self, planet: Planet) -> None:
        self.children.append(planet)
        if len(self.children) > 1:

    def set_parent(self, parent: Planet) -> None:
        self.parent = parent

    def get_path_length(self) -> int:
        if self.name == CENTER_OF_MASS: return 0
        length = 1
        pointer = self
        while pointer.parent.name != CENTER_OF_MASS:
            length += 1
            pointer = pointer.parent
        return length

input_lines = open("input/testinput6.txt").readlines()
orbit_map = [tuple(line.strip().split(")")) for line in input_lines]

planets = {}
for parent, child in orbit_map:
    if parent not in planets:
        planets[parent] = Planet(parent)
    if child not in planets:
        planets[child] = Planet(child)
    planets[parent].add_child(planets[child])
    planets[child].set_parent(planets[parent])

# Sum of length of paths to all nodes in tree
print(sum([planet.get_path_length() for planet in planets.values()]))
