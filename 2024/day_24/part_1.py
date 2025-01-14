def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def init(lines: list[str]) -> tuple[list[str], list[str]]:
    inputs, operations = [], []

    for line in lines:
        if ":" in line:
            inputs.append(line)

        if "->" in line:
            operations.append(line)

    return inputs, operations


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    wires = {}
    z_wires = []
    op_map = {
        "AND": "&",
        "OR": "|",
        "XOR": "^",
    }

    inputs, operations = init(lines)

    for input in inputs:
        wire, value = input.split(": ")
        wires[wire] = int(value)

    i = 0
    while operations:
        operation = operations[i]
        exp = operation.split(" ")
        w1 = exp[0]
        op = exp[1]
        w2 = exp[2]
        out = exp[4]
        
        if w1 not in wires or w2 not in wires:
            i += 1
        else:
            value = eval(f"{wires[w1]} {op_map[op]} {wires[w2]}")
            wires[out] = value
            operations.remove(operation)
            i = 0

            if out.startswith("z"):
                z_wires.append((out, value))

    sorted_z_wires = sorted(z_wires, key=lambda x: x[0], reverse=True)

    binary = ""

    for wire in sorted_z_wires:
        binary += str(wire[1])

    total = int(binary, 2)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
