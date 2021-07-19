import instructions as ins

class BasicML:
    def __init__(self):
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0

    def validate_instruction(self, instruction):
        """ 
            private
            Validate a given instruction. Return True if the instruction is valid, False otherwise.
        """
        if instruction == 43:
            return True
        if (instruction < 1000 or instruction > 4299):
            return False
        return (instruction // 100) in [10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42]

    def validate_user_input(self):
        """
            private
            Validate user input. Should always be a negative or positive integer with a maximum of 4 
            digits. Return True if valid, False otherwise.
        """  
        pass

    def run_instruction(self):

        """ 
            Jarrett Minton
            private
            Run the next instruction, which should be in the instruction register when this is called.
        """
        self.operation_code = self.instruction_register // 100
        self.operand = self.instruction_register % 100

        if self.operation_code == 10:
            ins.read(self.memory, self.operation_code)
        elif self.operation_code == 11:
            ins.write(self.memory, self.operation_code)
        elif self.operation_code == 20:
            ins.load(self.memory, self.operation_code)
        elif self.operation_code == 21:
            ins.store(self.memory, self.operation_code, self.accumulator)


        elif self.operation_code == 30:
            self.accumulator = ins.add(self.memory, self.operation_code, self.accumulator)
        elif self.operation_code == 31:
            self.accumulator = ins.subtract(self.memory, self.operation_code, self.accumulator)
        elif self.operation_code == 32:
            self.accumulator = ins.divide(self.memory, self.operation_code, self.accumulator)
        elif self.operation_code == 33:
            self.accumulator = ins.multiply(self.memory, self.operation_code, self.accumulator)

        elif self.operation_code == 40:
            self.instruction_counter = ins.branch(self.operation_code)
        elif self.operation_code == 41:
            self.instruction_counter = ins.branchneg(self.operation_code, self.accumulator)
        elif self.operation_code == 42:
            self.instruction_counter = ins.branchzero(self.operation_code, self.accumulator)
        
        elif self.operation_code == 43:
            ins.halt()
        


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
                    b.  If the instruction is valid, put it in the instruction register, then increment the
                        instruction counter and call run_instruction
                    c.  If the instruction is invalid, print an appropriate error and stops execution
                    d.  If a HALT instruction is reached, an appropriate message should be printed and execution
                        should be stopped.
        """
        self.instruction_counter = 0
        while True:
            currentInstruction = self.memory[self.instruction_counter]
            if currentInstruction == 43:
                print('*** Run completed ***')
                break

            elif self.validate_instruction(currentInstruction):
                self.instruction_register = currentInstruction
                self.instruction_counter += 1
                self.run_instruction()

            else:
                self.log_error(f"Instruction in memory location {self.instruction_counter:02} is invalid. Unable to continue execution")
                break
