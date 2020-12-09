from collections import defaultdict
from copy import deepcopy

instructions = [line.strip().split() for line in open('08-input.txt').readlines()]

def run_program(instructions):
    program_size = len(instructions) - 1
    executed_instructions = defaultdict(int)
    accumulator = 0
    ip = 0
    while True:
        if ip in executed_instructions:
            # part 1, read accumulator here
            return -1   
        if ip > program_size:
            return accumulator

        instruction = instructions[ip][0]
        number = int(int(instructions[ip][1]))

        if instruction == 'acc':
            accumulator += number
        elif instruction == 'jmp':
            executed_instructions[ip] += 1
            ip += number
            continue

        executed_instructions[ip] += 1
        ip += 1

for i in range(len(instructions)):
    if instructions[i][0] in ['nop', 'jmp']:
        modified_instructions = deepcopy(instructions)
        if instructions[i][0] == 'nop':
            new_instruction = modified_instructions[i]
            new_instruction[0] = 'jmp'
            modified_instructions[i] = new_instruction

        elif instructions[i][0] == 'jmp':
            new_instruction = modified_instructions[i]
            new_instruction[0] = 'nop'
            modified_instructions[i] = new_instruction

        acc = run_program(modified_instructions)
        if acc > -1:
            print(acc)
            break