#!/usr/bin/env python
import numpy as np

class Claim:
    def __init__(self, id, pos, size):
        self.id = id
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.width = int(size[0])
        self.height = int(size[1])

class Grid:
    def __init__(self, claims, width=1100, height=1100):
        self.grid = np.zeros((width, height))
        self.claims = claims
        for claim in claims:
            self.grid[claim.x:claim.x+claim.width, claim.y:claim.y+claim.height] += 1

    def count_overlaps(self):
        overlapping_fields = self.grid > 1
        return np.unique(overlapping_fields, return_counts=True)[1][1]

    def find_no_overlap_id(self):
        no_overlap = self.grid == 1
        for claim in self.claims:
            if no_overlap[claim.x:claim.x+claim.width, claim.y:claim.y+claim.height].all():
                return claim.id


def read_claims(input_file):
    """
    Read input file and return an array of Claim objects containing position and size
    """
    claims = []
    with open(input_file) as input:
        for line in input:
            id, _, pos, size = line.split(" ")
            id = id[1:]
            x, y = pos.split(',')
            y = y[:-1]
            width, height = size.split('x')
            height = height[:-1]
            claims.append(Claim(id, (x, y), (width, height)))
    return claims

if __name__ == "__main__":
    claims = read_claims("input.txt")
    grid = Grid(claims)
    print("Overlapping square inches:", grid.count_overlaps())
