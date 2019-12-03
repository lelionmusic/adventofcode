#!/usr/bin/env python

def find_box(input_file):
    """
    Read in the lines of input_file to a list, then find two lines which only
    differs by one character. It is assumed all lines are of equal length.

    Return a two-tuple with the two lines (line1, line2)
    """
    box_ids = [] 
    with open(input_file) as input:
        for line in input:
            box_ids.append(line.strip())
    
    for index, id in enumerate(box_ids):
        for id2 in box_ids:
            same_char_count = 0
            for char_nr, char in enumerate(id):
                if id2[char_nr] == id[char_nr] and id != id2: 
                    same_char_count += 1
                    if same_char_count == len(id) - 1: 
                        return (id, id2)
            
print(find_box("input.txt"))
