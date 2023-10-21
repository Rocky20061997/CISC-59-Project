# Version 1
class Simpletron:
    def __init__(self):
        self.memory = [0] * 100
        self.accumulator = 0
        self.instructionCounter = 0

    def execute(self, program):
        # Load program into memory
        for index, instruction in enumerate(program):
            self.memory[index] = instruction

        while True:
            instruction = self.memory[self.instructionCounter]

            operation_code = instruction // 100
            operand = instruction % 100

            if operation_code == 10:  # READ
                self.memory[operand] = int(input("Enter a number: "))
            elif operation_code == 11:  # WRITE
                print(self.memory[operand])
            elif operation_code == 20:  # LOAD
                self.accumulator = self.memory[operand]
            elif operation_code == 21:  # STORE
                self.memory[operand] = self.accumulator
            elif operation_code == 30:  # ADD
                self.accumulator += self.memory[operand]
            elif operation_code == 43:  # HALT
                break

            self.instructionCounter += 1

program = [1007, 1008, 2007, 3008, 2109, 1109, 4300]
s = Simpletron()
s.execute(program)
