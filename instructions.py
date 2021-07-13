'''
Instruction methods for VM
By Jarrett Minton, Utah Valley University
'''

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

def add(memory, operand, accum):
    '''Add a word from a specific location in memory
    to the word in the accumulator and leave the result
    in the accumula'''
    mem_loc = mem_loc_gen(operand)
    word_to_add = int(memory[mem_loc])
    return str(int(accum) + word_to_add)

def subtract(memory, operand, accum):
    '''Subtract a word from a specific location in memory 
    from the word in the accumulator and leave the result
     in the accumulato'''
    mem_loc = mem_loc_gen(operand)
    word_to_subtract = int(memory[mem_loc])
    return str(int(accum) - word_to_subtract)

def divide(memory, operand, accum):
    '''Divide the word in the accumulator by a word from a 
    specific location in memory and leave the result in the 
    accumulator'''
    mem_loc = mem_loc_gen(operand)
    word_to_divide = int(memory[mem_loc])
    return str(int(accum) / word_to_divide)

def multiply(memory, operand, accum):
    '''Multiply a word from a specific location in memory to 
    the word in the accumulator and leave the result in the
    accumulato'''
    mem_loc = mem_loc_gen(operand)
    word_to_multi = int(memory[mem_loc])
    return str(int(accum) * word_to_multi)