from itertools import permutations

OP_ADD = 1
OP_MULT = 2
OP_WRITE = 3
OP_READ = 4
OP_JNZ = 5
OP_JZ = 6
OP_LESS = 7
OP_EQUALS = 8
OP_ADJUST = 9
OP_HALT = 99
MODE_POSITION = 0
MODE_IMMEDIATE = 1
MODE_RELATIVE = 2

class IntcodeComputer:
    def __init__(self, data, phase=None, mem_size=100000):
        self.ip = 0
        self.base = 0
        self.mem = data.copy()
        self.mem += [0] * mem_size
        self.started = False
        self.phase = phase

    def add(self, params):
        self.mem[params[2]] = self.mem[params[0]] + self.mem[params[1]]

    def mult(self, params):
        self.mem[params[2]] = self.mem[params[0]] * self.mem[params[1]]

    def write(self, input_signal, params):
        self.mem[params[0]] = input_signal

    def read(self, params):
        return self.mem[params[0]]

    def jnz(self, params):
        self.ip = self.mem[params[1]] if self.mem[params[0]] != 0 else self.ip + 3

    def jz(self, params):
        self.ip = self.mem[params[1]] if self.mem[params[0]] == 0 else self.ip + 3

    def less(self, params):
        self.mem[params[2]] = 1 if self.mem[params[0]] < self.mem[params[1]] else 0

    def equals(self, params):
        self.mem[params[2]] = 1 if self.mem[params[0]] == self.mem[params[1]] else 0

    def adjust_base(self, params):
        self.base += self.mem[params[0]]

    def get_addr(self, offset):
        instruction = self.mem[self.ip]
        mode = (instruction % (1000 * 10**offset) - (instruction % 100)) // (100 * 10**offset)
        if mode == MODE_IMMEDIATE:
            return self.ip + 1 + offset
        if mode == MODE_POSITION:
            return self.mem[self.ip + 1 + offset]
        return self.mem[self.ip + 1 + offset] + self.base

    def execute(self, input_signal=None):
        param_lengths = [4, 4, 2, 2, 2, 2, 4, 4, 2]
        current_input_signal = input_signal
        while True:
            if input_signal != None and self.phase != None:
                current_input_signal = input_signal if self.started else self.phase
            self.started = True

            opcode = self.mem[self.ip] % 100
            params = [self.get_addr(i) for i in range(param_lengths[opcode - 1])]

            if opcode == OP_ADD:      self.add(params)
            elif opcode == OP_MULT:   self.mult(params)
            elif opcode == OP_WRITE:  self.write(current_input_signal, params)
            elif opcode == OP_READ:   return self.read(params)
            elif opcode == OP_JNZ:    self.jnz(params)
            elif opcode == OP_JZ:     self.jz(params)
            elif opcode == OP_LESS:   self.less(params)
            elif opcode == OP_EQUALS: self.equals(params)
            elif opcode == OP_ADJUST: self.adjust_base(params)
            elif opcode == OP_HALT:
                return (input_signal, OP_HALT)

            # Increment IP unless it was as jump instruction
            if opcode not in [OP_JNZ, OP_JZ]:
                self.ip += param_lengths[opcode - 1]

            if opcode == OP_HALT:
                return (input_signal, OP_HALT)
