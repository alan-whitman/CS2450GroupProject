'''Instruction methods for VM.'''

def mem_loc_gen(location):
    '''Generate memory location from operand string.'''
    mem_loc = str(location)
    if mem_loc[0:1] == '0':
        mem_loc = mem_loc[1:]
    if mem_loc[0:1] == '0':
        mem_loc = mem_loc[1:]
    mem_loc = int(mem_loc)
    return mem_loc

def read(memory, operand):
    '''Reads a word from the keyboard into
    the specific location in memory.'''
    mem_loc = mem_loc_gen(operand)
    read = input("READ >> ")
    memory[mem_loc] = read

def write(memory, operand):
    '''Write a word from the specific location 
    in memory to screen.'''
    mem_loc = mem_loc_gen(operand)
    print("WRITE >> " + memory[mem_loc])

def load(memory, operand):
    '''Load a word from a specific location in memory. 
    MAKE SURE TO INSTANTIATE ACCUMULATOR TO THIS FUNC'''
    mem_loc = mem_loc_gen(operand)
    return memory[mem_loc]

def store(memory, operand, accum):
    '''Store a word from the accumulator into a 
    specific location in memory.'''
    mem_loc = mem_loc_gen(operand)
    memory[mem_loc] = accum


