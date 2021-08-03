from abc import ABC, abstractmethod


class Operator(ABC):
    @abstractmethod
    def execute(self, bml):
        pass


class Read(Operator):
    def validate_user_input(self, user_input):
        try:
            n = int(user_input)
            if n < -9999 or n > 9999:
                return False
            return True
        except:
            return False

    def execute(self, bml):
        is_valid_input = False
        while not is_valid_input:
            user_input = input("Enter an integer: ")
            if (self.validate_user_input(user_input)):
                bml.memory[bml.operand] = int(user_input)
                is_valid_input = True
            else:
                print("Invalid input (must be a number between -9999 and 9999).")


class Multiply(Operator):
    def execute(self, bml):
        bml.accumulator = bml.memory[bml.operand] * bml.accumulator


class Store(Operator):
    def execute(self, bml):
        bml.memory[bml.operand] = bml.accumulator


class WriteAscii(Operator):
    def execute(self, bml):
        instruction = str(bml.memory[bml.operand])
        ascii_symbol = instruction[2:]
        if ascii_symbol[0] == '0':
            ascii_symbol = int(instruction[3:])
        if ascii_symbol[0] == '0' and ascii_symbol[1] == '0':
            ascii_symbol = int(instruction[4])
        print(chr(ascii_symbol))


class Subtract(Operator):
    def execute(self, bml):
        bml.accumulator = bml.accumulator - bml.memory[bml.operand]


class BranchZero(Operator):
    def execute(self, bml):
        if bml.accumulator == 0:
            bml.instruction_count = bml.operand
