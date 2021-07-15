class BasicML:
    def __init__(self):
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0
        self.opcodes = {
            'READ': 10, 
            'WRITE': 11, 
            'LOAD': 20, 
            'STORE': 21,
            'ADD': 30, 
            'SUBTRACT': 31, 
            'DIVIDE': 32, 
            'MULTIPLY': 33, 
            'BRANCH': 40, 
            'BRANCHNEG': 41,
            'BRANCHZERO': 42,
            'HALT': 43
        }

    def validate_instruction(self, instruction):
        """ 
            private
            Validate a given instruction. Return True if the instruction is valid, False otherwise.
        """
        return instruction in self.opcodes or isinstance(instruction, int)

    def validate_user_input(self):
        """
            private
            Validate user input. Should always be a negative or positive integer with a maximum of 4 
            digits. Return True if valid, False otherwise.
        """  

    def run_instruction(self):

        """ 
            Jarrett Minton
            private
            Run the next instruction, which should be in the instruction register when this is called.
        """
        pass

    def log_error(self, error_msg):
        """  
            Jarrett Minton
            private
            Print an error to the console in a standardized format
        """
        print("ERROR: " + error_msg)

    def dump(self):
        """ 
            public
            Dump register and memory to console, as per spec. 
        """
        pass

    def initial_prompt(self):
        """ 
            public
            Print out initial prompt with instructions, as per spec 
        """
        pass

    def validate_program(self):
        """
            public
            Validates each instruction in the program. If errors are found, prints appropriate error messages.
            Returns True if each instruction is valid, False otherwise.
            Assumes that the last instruction entered is the one immediately before whatever instruction_counter
            points to.
        """
        program_is_valid = True
        for i in range(0, self.instruction_counter):
            instruction_is_valid = self.validate_instruction(self.memory[i])
            if not instruction_is_valid:
                program_is_valid = False
                self.log_error(f"Instruction in memory location {i:02} is invalid")
        return program_is_valid

    def get_next_instruction(self):
        """ 
            public
            Needs to:
                1.  Display the memory location where the next instruction would live, 
                    then get the next instruction
                2.  Wait for user keyboard input
                3.  Validate each instruction after it is input. If the instruction is invalid, it should 
                    display an error, then prompt again for the same memory location. If it is valid, the
                    instruction should be stored in the corresponding memory location, and the instruction
                    counter should be incremented.
                4.  Return false once the user inputs -99999
        """
        print(f"{self.instruction_counter:02} ? ", end="")
        user_input = input()
        if user_input == "-99999":
            return False
        instruction = 0
        try:
            instruction = int(user_input)
        except:
            instruction = -1
        self.memory[self.instruction_counter] = instruction
        self.instruction_counter += 1
        return True

    def run_program(self):
        """ 
            public
            Needs to do the following:
                1.  Reset the instrucion counter to 0
                2.  Start a loop that does the following:
                    a.  Validates the instruction at the location of the instruction counter.
                    b.  If the instruction is valid, put it in the instruction register, then call run_instruction
                    c.  If the instruction is invalid, print an appropriate error and stops execution
                    d.  If a HALT instruction is reached, an appropriate message should be printed and execution
                        should be stopped.
                    e.  Increment the instruction counter.
        """

        self.instruction_counter = 0
        while True:
            currentInstruction = self.memory[self.instruction_counter]
            if currentInstruction == 43:
                print('*** Run completed ***')
                break

            elif self.validate_instruction(currentInstruction):
                self.instruction_register = currentInstruction
                self.run_instruction(currentInstruction)
                self.instruction_counter += 1

            else:
                self.log_error('Instruction invalid.')
                break
        pass
