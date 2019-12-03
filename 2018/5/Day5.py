#!/usr/bin/env python
import re
from string import ascii_lowercase

alphabet = ascii_lowercase

# Making the regex (aA|Aa|bB|Bb ...)
reg = "("
for char in alphabet:
    reg += char + char.upper() + "|" + char.upper() + char + "|"
reg = reg[:-1] + ")"

# Read the polymer as a string
with open("input.txt") as input:
    original_polymer = input.read().rstrip()

# Run the replacement algorithm 26 times, one for every letter
lowest_length = -1
for char in alphabet:
    polymer = re.sub(char, '', original_polymer, flags=re.IGNORECASE)
    print("Removing", char)

    while (True):
        next_polymer = re.sub(reg, '', polymer)
        if polymer == next_polymer: break
        polymer = next_polymer

    length = len(polymer)
    print(length)

    if length < lowest_length or lowest_length == -1:
        lowest_length = length

print("Lowest length:", lowest_length)

