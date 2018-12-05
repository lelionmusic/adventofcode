#!/usr/bin/env python

def find_checksum(input_file):
    two_letters = 0
    three_letters = 0
    with open(input_file) as input:
        for line in input:
            if exactly_n(line, 2): two_letters += 1
            if exactly_n(line, 3): three_letters += 1
    return two_letters * three_letters
            
def exactly_n(string, n):
    for char in string:
        if string.count(char) == n: return True
    return False

print(find_checksum("input.txt"))
