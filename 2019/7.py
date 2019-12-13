from itertools import permutations

data = [int(x) for x in open("input/input7.txt").read().split(',')]

OP_ADD = 1
OP_MULT = 2
OP_WRITE = 3
OP_READ = 4
OP_JNZ = 5
OP_JZ = 6
OP_LESS = 7
OP_EQUALS = 8
OP_HALT = 99
MODE_POSITION = 0
MODE_IMMEDIATE = 1

class IntcodeComputer:
    def __init__(self, data, phase):
        self.ip = 0
        self.mem = data.copy()
        self.started = False
        self.phase = phase

    def add(self):
        param1 = get_param(self.mem, self.ip, 0)
        param2 = get_param(self.mem, self.ip, 1)
        addr = self.mem[self.ip+3]
        self.mem[addr] = param1 + param2
        self.ip += 4

    def mult(self):
        param1 = get_param(self.mem, self.ip, 0)
        param2 = get_param(self.mem, self.ip, 1)
        addr = self.mem[self.ip+3]
        self.mem[addr] = param1 * param2
        self.ip += 4

    def write(self, input_signal):
        addr = self.mem[self.ip+1]
        self.mem[addr] = int(input_signal)
        self.ip += 2

    def read(self):
        addr = self.mem[self.ip+1]
        self.ip += 2
        return self.mem[addr]

    def jnz(self):
        param1 = get_param(self.mem, self.ip, 0)
        param2 = get_param(self.mem, self.ip, 1)
        if param1 != 0:
            self.ip = param2
        else: self.ip +=3

    def jz(self):
        param1 = get_param(self.mem, self.ip, 0)
        param2 = get_param(self.mem, self.ip, 1)
        if param1 == 0:
            self.ip = param2
        else: self.ip +=3

    def less(self):
        param1 = get_param(self.mem, self.ip, 0)
        param2 = get_param(self.mem, self.ip, 1)
        addr = self.mem[self.ip+3]
        if param1 < param2:
            self.mem[addr] = 1
        else:
            self.mem[addr] = 0
        self.ip += 4

    def equals(self):
        param1 = get_param(self.mem, self.ip, 0)
        param2 = get_param(self.mem, self.ip, 1)
        addr = self.mem[self.ip+3]
        if param1 == param2:
            self.mem[addr] = 1
        else:
            self.mem[addr] = 0
        self.ip += 4
        

    def execute(self, input_signal):
        while True:
            current_input_signal = input_signal if self.started else self.phase
            self.started = True
            opcode = self.mem[self.ip] % 100
            if opcode == OP_ADD:
                self.add()
            elif opcode == OP_MULT:
                self.mult()
            elif opcode == OP_WRITE:
                self.write(current_input_signal)
            elif opcode == OP_READ:
                return self.read()
            elif opcode == OP_JNZ:
                self.jnz()
            elif opcode == OP_JZ:
                self.jz()
            elif opcode == OP_LESS:
                self.less()
            elif opcode == OP_EQUALS:
                self.equals()
            elif opcode == OP_HALT:
                return (input_signal, OP_HALT)

def get_param(mem, ip, offset, signal = None):
    instruction = mem[ip]
    factor = 1
    if offset == 1: factor = 10
    mode = (instruction % (1000 * factor ) - (instruction % 100)) // (100 * factor)
    if mode == MODE_IMMEDIATE:
        return mem[ip+1+offset]
    return mem[mem[ip+1+offset]]

def run_amplifiers(phases):
    computers = [IntcodeComputer(data, phases[i]) for i in range(5)]
    signal = 0
    while True:
        for i in range(5):
            signal = computers[i].execute(signal)
            if type(signal) == tuple and signal[1] == OP_HALT:
                return signal[0]

phases = [[int(p) for p in phases] for phases in permutations("01234")]
print("Part 1:", max(run_amplifiers(p) for p in phases))

phases2 = [list(map(lambda x: x + 5, p)) for p in phases]
print("Part 2:", max(run_amplifiers(p) for p in phases2))
