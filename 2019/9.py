from intcode import *

data = [int(x) for x in open("input/input9.txt").read().split(",")]
computer = IntcodeComputer(data)
output = computer.execute(input_signal=2)
print(output)
