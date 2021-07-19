'''
Instruction methods for VM
By Jarrett Minton, Utah Valley University
'''

def validate_user_input(user_input):
    """
        Validate user input. Should always be a negative or positive integer with a maximum of 4 
        digits. Return True if valid, False otherwise.
    """
    try:
        n = int(user_input)
        if n < -9999 or n > 9999:
            return False
        return True
    except:
        return False

def read(memory, operand):
    '''Reads a word from the keyboard into
    the specific location in memory.'''
    is_valid_input = False
    while not is_valid_input:
        user_input = input("Enter an integer: ")
        if (validate_user_input(user_input)):
            memory[operand] = int(user_input)
            is_valid_input = True
        else:
            print("Invalild input.")

def write(memory, operand):
    '''Write a word from the specific location 
    in memory to screen.'''
    print(f"Contents of {operand} is {memory[operand]}")

def load(memory, operand):
    '''Load a word from a specific location in memory. 
    MAKE SURE TO INSTANTIATE ACCUMULATOR TO THIS FUNC'''
    return memory[operand]

def store(memory, operand, accum):
    '''Store a word from the accumulator into a 
    specific location in memory.'''
    memory[operand] = accum

def add(memory, operand, accum):
    '''Add a word from a specific location in memory
    to the word in the accumulator and leave the result
    in the accumula'''
    word_to_add = memory[operand]
    return accum + word_to_add

def subtract(memory, operand, accum):
    '''Subtract a word from a specific location in memory 
    from the word in the accumulator and leave the result
     in the accumulato'''
    word_to_subtract = memory[operand]
    return accum - word_to_subtract

def divide(memory, operand, accum):
    '''Divide the word in the accumulator by a word from a 
    specific location in memory and leave the result in the 
    accumulator'''
    word_to_divide = memory[operand]
    return accum // word_to_divide

def multiply(memory, operand, accum):
    '''Multiply a word from a specific location in memory to 
    the word in the accumulator and leave the result in the
    accumulato'''
    word_to_multi = memory[operand]
    return accum * word_to_multi

def branch(operand):
    '''Branch to a specific location in memory
       Set to counter.
    '''
    return operand

def branchneg(operand, accum, current_instruction_counter):
    '''Branch to a specific location in memory if the accumulator is negative'''
    if accum < 0:
        return operand
    return current_instruction_counter

def branchzero(operand, accum, current_instruction_counter):
    '''Branch to a specific location in memory if the accumulator is zero'''
    if accum == 0:
        return operand
    return current_instruction_counter
