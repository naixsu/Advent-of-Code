def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


class Computer:
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.a = None
        self.b = None
        self.c = None
        self.program = None

        self.init_computer()

    def print_instructions(self) -> None:
        print(f"A: {self.a}, B: {self.b}, C: {self.c}, Ins: {self.program}")


    def init_computer(self) -> None:
        for line in self.lines:
            if line.startswith("Register A:"):
                self.a = int(line.split(":")[1].strip())
            elif line.startswith("Register B:"):
                self.b = int(line.split(":")[1].strip())
            elif line.startswith("Register C:"):
                self.c = int(line.split(":")[1].strip())
            elif line.startswith("Program:"):
                self.program = list(map(int, line.split(":")[1].strip().split(",")))


    def get_combo(self, operand: int) -> int:
        if operand == 7:
            return -1
        if operand <= 3:
            return operand

        combo_map = {
            4: self.a,
            5: self.b,
            6: self.c
        }

        return combo_map[operand]


    def get_output(self) -> str:
        output = ""
        ip = 0
        output = []

        while ip < len(self.program):
            opcode = self.program[ip]
            operand = self.program[ip + 1]

            match opcode:
                case 0: # adv
                    self.a = int(self.a / (2 ** self.get_combo(operand)))
                case 1: # bxl
                    self.b = self.b ^ operand
                case 2: # bst
                    self.b = self.get_combo(operand) % 8
                case 3: # jnz
                    if self.a != 0:
                        ip = operand - 2
                case 4: # bxc
                    self.b = self.b ^ self.c
                case 5: # out
                    output.append(str(self.get_combo(operand) % 8))
                case 6: # bdv
                    self.b = int(self.a / (2 ** self.get_combo(operand)))
                case 7: # cdv
                    self.c = int(self.a / (2 ** self.get_combo(operand)))

            ip += 2

        return ','.join(output)


def get_output() -> None:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    computer = Computer(lines)
    output = computer.get_output()

    print(output)


def main() -> None:
    get_output()


if __name__ == "__main__":
    main()
