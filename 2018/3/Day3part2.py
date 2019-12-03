#!/usr/bin/env python
from Day3part1 import *

if __name__ == "__main__":
    claims = read_claims("input.txt")
    grid = Grid(claims)
    print(grid.find_no_overlap_id())
