original_data = open("input/input2.txt").read().split(',')
original_data = [int(x) for x in original_data]

def execute(data):
    IP = 0
    while data[IP] != 99:
        if data[IP] == 1:
            data[data[IP+3]] = data[data[IP+1]] + data[data[IP+2]]
        elif data[IP] == 2:
            data[data[IP+3]] = data[data[IP+1]] * data[data[IP+2]]
        IP += 4

def apply_input(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb

def find_output(data, output):
    for noun in range(100):
        for verb in range(100):
            memory = data.copy()
            apply_input(memory, noun, verb)
            execute(memory)
            if memory[0] == output:
                return noun, verb


memory = original_data.copy()
apply_input(memory, 12, 2)
execute(memory)
print("Part 1:", memory[0])

noun, verb = find_output(original_data, 19690720)
print("Part 2: noun =", noun, "verb =", verb)
