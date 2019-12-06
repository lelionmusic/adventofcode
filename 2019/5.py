original_data = open("input/input5.txt").read().split(',')
original_data = [int(x) for x in original_data]

OP_ADD = 1
OP_MULT = 2
OP_WRITE = 3
OP_READ = 4
OP_JNZ = 5
OP_JZ = 6
OP_LESS = 7
OP_EQUALS = 8

MODE_POSITION = 0
MODE_IMMEDIATE = 1

ip = 0

def add(data):
    global ip
    param1 = get_param(data, 0)
    param2 = get_param(data, 1)
    addr = data[ip+3]
    data[addr] = param1 + param2
    ip += 4

def mult(data):
    global ip
    param1 = get_param(data, 0)
    param2 = get_param(data, 1)
    addr = data[ip+3]
    data[addr] = param1 * param2
    ip += 4

def write(data):
    global ip
    addr = data[ip+1]
    data[addr] = int(input("Waiting for input..."))
    ip += 2

def read(data):
    global ip
    addr = data[ip+1]
    print(data[addr])
    ip += 2

def jnz(data):
    global ip
    param1 = get_param(data, 0)
    param2 = get_param(data, 1)
    if param1 != 0:
        ip = param2
    else: ip +=3

def jz(data):
    global ip
    param1 = get_param(data, 0)
    param2 = get_param(data, 1)
    if param1 == 0:
        ip = param2
    else: ip +=3

def less(data):
    global ip
    param1 = get_param(data, 0)
    param2 = get_param(data, 1)
    addr = data[ip+3]
    if param1 < param2:
        data[addr] = 1
    else:
        data[addr] = 0
    ip += 4

def equals(data):
    global ip
    param1 = get_param(data, 0)
    param2 = get_param(data, 1)
    addr = data[ip+3]
    if param1 == param2:
        data[addr] = 1
    else:
        data[addr] = 0
    ip += 4

def get_param(data, offset):
    instruction = data[ip]
    factor = 1
    if offset == 1: factor = 10
    mode = (instruction % (1000 * factor ) - (instruction % 100)) // (100 * factor)
    if mode == MODE_IMMEDIATE:
        return data[ip+1+offset]
    return data[data[ip+1+offset]]

def execute(data):
    while data[ip] % 100 != 99:
        instruction = data[ip]
        opcode = instruction % 100
        if opcode == OP_ADD:
            add(data)
        elif opcode == OP_MULT:
            mult(data)
        elif opcode == OP_READ:
            read(data)
        elif opcode == OP_WRITE:
            write(data)
        elif opcode == OP_JNZ:
            jnz(data)
        elif opcode == OP_JZ:
            jz(data)
        elif opcode == OP_LESS:
            less(data)
        elif opcode == OP_EQUALS:
            equals(data)

execute(original_data)
