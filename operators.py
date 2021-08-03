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

class Write(Operator):
    def execute(self, bml):
        print(f"Contents of {bml.operand} is {bml.memory[bml.operand]}")

class Load(Operator):
    def execute(self, bml):
        bml.accumulator = bml.memory[bml.operand]

class Store(Operator):
    def execute(self, bml):
        bml.memory[bml.operand] = bml.accumulator

class SetAccum(Operator):
    def execute(self, bml):
        bml.accumulator = bml.operand

class Add(Operator):
    def execute(self, bml):
       bml.accumulator = bml.memory[bml.operand] + bml.accumulator

class Divide(Operator):
    def execute(self, bml):
        bml.accumulator = bml.accumulator // bml.memory[bml.operand]

class Multiply(Operator):
    def execute(self, bml):
        bml.accumulator = bml.memory[bml.operand] * bml.accumulator

class Branch(Operator):
    def execute(self, bml):
        bml.instruction_counter = bml.operand

class BranchNeg(Operator):
    def execute(self, bml):
        if bml.accumulator < 0:
            bml.instruction_counter = bml.operand
