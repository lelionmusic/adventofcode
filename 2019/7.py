from itertools import permutations
from intcode import *

def run_amplifiers(data, phases):
    computers = [IntcodeComputer(data, phases[i]) for i in range(5)]
    signal = 0
    while True:
        for i in range(5):
            signal = computers[i].execute(signal)
            if type(signal) == tuple and signal[1] == OP_HALT:
                return signal[0]


if __name__ == "__main__":
    data = [int(x) for x in open("input/input7.txt").read().split(",")]

    phases = [[int(p) for p in phases] for phases in permutations("01234")]
    print("Part 1:", max(run_amplifiers(data, p) for p in phases))

    phases2 = [list(map(lambda x: x + 5, p)) for p in phases]
    print("Part 2:", max(run_amplifiers(data, p) for p in phases2))
