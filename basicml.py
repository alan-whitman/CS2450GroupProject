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
        pass

    def validate_user_input(self):
        """
            private
            Validate user input. Should always be a negative or positive integer with a maximum of 4 
            digits. Return True if valid, False otherwise.
        """

    def run_instruction(self):
        """ 
            private
            Run the next instruction, which should be in the instruction register when this is called.
        """
        pass

    def log_error(self, error_msg):
        """  
            private
            Print an error to the console in a standardized format
        """
        pass

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
        pass

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
        pass
