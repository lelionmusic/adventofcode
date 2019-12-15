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
        self.mem = [0] * mem_size
        self.mem[: len(data)] = data.copy()
        self.started = False
        self.phase = phase

    def add(self):
        param1 = get_param(self.mem, self.ip, 0, base=self.base)
        param2 = get_param(self.mem, self.ip, 1, base=self.base)
        addr = get_addr(self.mem, self.ip, 2, self.base)
        self.mem[addr] = param1 + param2
        self.ip += 4

    def mult(self):
        param1 = get_param(self.mem, self.ip, 0, base=self.base)
        param2 = get_param(self.mem, self.ip, 1, base=self.base)
        addr = get_addr(self.mem, self.ip, 2, self.base)
        self.mem[addr] = param1 * param2
        self.ip += 4

    def write(self, input_signal):
        addr = get_addr(self.mem, self.ip, 0, base=self.base)
        self.mem[addr] = int(input_signal)
        self.ip += 2

    def read(self):
        param1 = get_param(self.mem, self.ip, 0, base=self.base)
        self.ip += 2
        return param1

    def jnz(self):
        param1 = get_param(self.mem, self.ip, 0, base=self.base)
        param2 = get_param(self.mem, self.ip, 1, base=self.base)
        if param1 != 0:
            self.ip = param2
        else:
            self.ip += 3

    def jz(self):
        param1 = get_param(self.mem, self.ip, 0, base=self.base)
        param2 = get_param(self.mem, self.ip, 1, base=self.base)
        if param1 == 0:
            self.ip = param2
        else:
            self.ip += 3

    def less(self):
        param1 = get_param(self.mem, self.ip, 0, base=self.base)
        param2 = get_param(self.mem, self.ip, 1, base=self.base)
        addr = get_addr(self.mem, self.ip, 2, self.base)
        if param1 < param2:
            self.mem[addr] = 1
        else:
            self.mem[addr] = 0
        self.ip += 4

    def equals(self):
        param1 = get_param(self.mem, self.ip, 0, base=self.base)
        param2 = get_param(self.mem, self.ip, 1, base=self.base)
        # addr = self.mem[self.ip + 3]
        addr = get_addr(self.mem, self.ip, 2, self.base)
        if param1 == param2:
            self.mem[addr] = 1
        else:
            self.mem[addr] = 0
        self.ip += 4

    def adjust_base(self):
        param1 = get_param(self.mem, self.ip, 0, base=self.base)
        self.base += param1
        self.ip += 2

    def execute(self, input_signal=None):
        current_input_signal = input_signal
        while True:
            opcode = self.mem[self.ip] % 100
            if input_signal != None and self.phase != None:
                current_input_signal = input_signal if self.started else self.phase
            self.started = True
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
            elif opcode == OP_ADJUST:
                self.adjust_base()
            elif opcode == OP_HALT:
                return (input_signal, OP_HALT)


def get_param(mem, ip, offset, signal=None, base=None):
    instruction = mem[ip]
    # TODO change to 10^offset
    factor = 1
    if offset == 1:
        factor = 10
    mode = (instruction % (1000 * factor) - (instruction % 100)) // (100 * factor)
    if mode == MODE_IMMEDIATE:
        return mem[ip + 1 + offset]
    if mode == MODE_POSITION:
        return mem[mem[ip + 1 + offset]]
    assert base != None
    return mem[mem[ip + 1 + offset] + base]

def get_addr(mem, ip, offset, base=None):
    instruction = mem[ip]
    factor = 1
    if offset == 1:
        factor = 10
    elif offset == 2:
        factor = 100
    mode = (instruction % (1000 * factor) - (instruction % 100)) // (100 * factor)
    if mode == MODE_IMMEDIATE:
        return ip + 1 + offset
    if mode == MODE_POSITION:
        return mem[ip + 1 + offset]
    assert base != None
    return mem[ip + 1 + offset] + base



def run_amplifiers(phases):
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
    print("Part 1:", max(run_amplifiers(p) for p in phases))

    phases2 = [list(map(lambda x: x + 5, p)) for p in phases]
    print("Part 2:", max(run_amplifiers(p) for p in phases2))
