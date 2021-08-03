import operators as ops

operators = {
    10: ops.Read(),
    12: ops.WriteAscii(),
    21: ops.Store(),
    31: ops.Subtract(),
    33: ops.Multiply(),
    42: ops.BranchZero()
}


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

    def run_instruction(self):
        """ 
            Jarrett Minton
            private
            Run the next instruction, which should be in the instruction register when this is called.
        """
        self.operation_code = self.instruction_register // 100
        self.operand = self.instruction_register % 100

        operators[self.operation_code].execute(self)

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

        print("REGISTERS:")
        print(f"Accumulator: {self.accumulator:05}")
        print(f"InstructionCounter: {self.instruction_counter:02}")
        print(f"InstructionRegister: {self.instruction_register:05}")
        print(f"OperationCode: {self.operation_code:02}")
        print(f"Operand: {self.operand:02}\n")

        print("MEMORY:")

        print("{:<3} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(
            "  ", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09"))

        x = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90"]

        count = 0
        for i in range(0, len(x)):
            print("{:<3} {:0>5} {:0>5} {:0>5} {:0>5} {:0>5} {:0>5} {:0>5} {:0>5} {:0>5} {:0>5}".format(
                x[i], self.memory[count], self.memory[count+1], self.memory[count+2], self.memory[count+3], self.memory[count+4], self.memory[count+5], self.memory[count+6], self.memory[count+7], self.memory[count+8], self.memory[count+9]))
            count += 10

    def initial_prompt(self):
        """ 
            public
            Print out initial prompt with instructions, as per spec 
        """
        print("*** Welcome to UVSim! ***")
        print("*** Please enter your program one instruction ***")
        print("*** (or data word) at a time into the input ***")
        print("*** text field. I will display the location ***")
        print("*** number and a question mark (?). You then ***")
        print("*** type the word for that location. Enter ***")
        print("*** -99999 to stop entering your program. ***")

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
                self.log_error(
                    f"Instruction in memory location {i:02} is invalid")
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
        if self.instruction_counter > 99:
            print("Maximum number of instructions reached.")
            return False
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
                print('\n*** Run completed ***\n')
                break

            elif self.validate_instruction(currentInstruction):
                self.instruction_register = currentInstruction
                self.instruction_counter += 1
                self.run_instruction()

            else:
                self.log_error(
                    f"Instruction in memory location {self.instruction_counter:02} is invalid. Unable to continue execution.")
                break
