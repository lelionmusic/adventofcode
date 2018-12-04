#!/usr/bin/env python

def first_reoccuring_freq(input_file):
    freq = 0
    previous_freqs = set()
    while (True):
        with open(input_file) as input:
            for line in input:
                freq += int(line)
                if (freq in previous_freqs):
                    return freq
                previous_freqs.add(freq)

if __name__ == "__main__":
    print(first_reoccuring_freq("1-1_input.txt"))
