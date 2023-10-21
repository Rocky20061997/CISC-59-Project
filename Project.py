class Simpletron:
    def __init__(self):
        self.memory = [0] * 100
        self.accumulator = 0
        self.instructionCounter = 0

    def load_program(self, program):
        for index, instruction in enumerate(program):
            self.memory[index] = instruction

    def execute(self):
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
            elif operation_code == 31:  # SUBTRACT
                self.accumulator -= self.memory[operand]
            elif operation_code == 32:  # DIVIDE
                if self.memory[operand] == 0:
                    print("Error: Division by zero!")
                    break
                self.accumulator //= self.memory[operand]
            elif operation_code == 33:  # MULTIPLY
                self.accumulator *= self.memory[operand]
            elif operation_code == 40:  # BRANCH
                self.instructionCounter = operand
                continue
            elif operation_code == 41:  # BRANCHNEG
                if self.accumulator < 0:
                    self.instructionCounter = operand
                    continue
            elif operation_code == 42:  # BRANCHZERO
                if self.accumulator == 0:
                    self.instructionCounter = operand
                    continue
            elif operation_code == 43:  # HALT
                print("Operation completed.")
                break

            self.instructionCounter += 1
            if self.instructionCounter >= len(self.memory):
                print("Error: Out of memory!")
                break

def main():
    s = Simpletron()
    while True:
        print("\nSimpletron Operations:")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Load program for addition
            program = [1007, 1008, 2007, 3008, 2109, 1109, 4300]
            s.load_program(program)
            s.execute()
        elif choice == 2:
            # Load program for subtraction
            program = [1007, 1008, 2007, 3108, 2109, 1109, 4300]
            s.load_program(program)
            s.execute()
        elif choice == 3:
            # Load program for multiplication
            program = [1007, 1008, 2007, 3308, 2109, 1109, 4300]
            s.load_program(program)
            s.execute()
        elif choice == 4:
            # Load program for division
            program = [1007, 1008, 2007, 3208, 2109, 1109, 4300]
            s.load_program(program)
            s.execute()
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()