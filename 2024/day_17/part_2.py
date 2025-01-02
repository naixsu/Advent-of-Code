def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


class Computer:
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.a = 0
        self.b = None
        self.b_og = None
        self.c = None
        self.c_og = None
        self.program = None

        self.init_computer()

    def print_instructions(self) -> None:
        print(f"A: {self.a}, B: {self.b}, C: {self.c}, Ins: {self.program}")


    def set_a(self, a: int) -> list[int]:
        self.a = a

        return self.get_output()

    def init_computer(self) -> None:
        for line in self.lines:
            if line.startswith("Register B:"):
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


    def get_output(self) -> list[int]:
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
                    output.append(int(self.get_combo(operand) % 8))
                case 6: # bdv
                    self.b = int(self.a / (2 ** self.get_combo(operand)))
                case 7: # cdv
                    self.c = int(self.a / (2 ** self.get_combo(operand)))

            ip += 2

        return output


def get_output() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")


    a_pots = [0]
    computer = Computer(lines)
    
    for i in range(len(computer.program)):
        pots = []

        for a in a_pots:
            for j in range(8):
                target = (a << 3) + j
                output = computer.set_a(target)

                if output == computer.program[-i-1:]:
                    pots.append(target)

        a_pots = pots

    return min(a_pots)


def main() -> None:
    output = get_output()
    print(output)


if __name__ == "__main__":
    main()
