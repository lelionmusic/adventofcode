#!/usr/bin/env python
import numpy as np

class Claim:
    def __init__(self, pos, size):
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.width = int(size[0])
        self.height = int(size[1])

    def overlaps(self, claim):
        return (self.x + self.width > claim.x and claim.x + claim.width > self.x and
                self.y + self.height > claim.y and claim.y + claim.height > self.y)

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
            claims.append(Claim((x, y), (width, height)))
    return claims

claims = read_claims("input.txt")
grid = np.zeros((1100,1100))
for claim in claims:
    grid[claim.x:claim.x+claim.width, claim.y:claim.y+claim.height] += 1

overlapping_fields = grid > 1
overlapping_sq_inches = np.unique(overlapping_fields, return_counts=True)[1][1]
print("Overlapping square inches:", overlapping_sq_inches)

