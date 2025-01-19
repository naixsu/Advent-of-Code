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


def get_ans():
    # I couldn't really figure this out on my own so I had to cheat a bit.
    # Thanks u/RobertOnReddit7
    # https://www.reddit.com/r/adventofcode/comments/1hqj35q/2024_day_24_part_2_c_very_proud_of_my_solution/

    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    inputs, operations = init(lines)

    gates = []

    for operation in operations:
        exp = operation.split(" ")
        w1 = exp[0]
        op = exp[1]
        w2 = exp[2]
        out = exp[4]

        gate = {
            "inputs": (w1, w2),
            "op": op,
            "output": out,
        }

        gates.append(gate)

    output_wires = [gate["output"] for gate in gates if gate["output"].startswith('z')]

    violations = []

    for gate in gates:
        # Starting gates should be followed by OR if AND, and by AND if XOR, except for the first one
        if (
            ( gate["inputs"][0].startswith("x") or gate["inputs"][1].startswith("x") ) and
            ( gate["inputs"][0].startswith("y") or gate["inputs"][1].startswith("y") ) and
            ( not "00" in gate["inputs"][0] and not "00" in gate["inputs"][1] )
        ):
            for second_gate in gates:
                if (
                    gate["output"] == second_gate["inputs"][0] or
                    gate["output"] == second_gate["inputs"][1]
                ):
                    if (
                        ( gate["op"] == "AND" and second_gate["op"] == "AND" ) or
                        ( gate["op"] == "XOR" and second_gate["op"] == "OR" )
                    ):
                        violations.append(gate["output"])
        # Gates in the middle should not have XOR operators
        if (
            not gate["inputs"][0].startswith("x") and not gate["inputs"][1].startswith("x") and
            not gate["inputs"][0].startswith("y") and not gate["inputs"][1].startswith("y") and
            not gate["output"].startswith("z") and gate["op"] == "XOR"
        ):
            violations.append(gate["output"])
        # Gates at the end should always have XOR operators, except for the last one
        if (
            gate["output"] in output_wires and
            gate["output"] != f"z{len(output_wires) - 1}" and
            gate["op"] != "XOR"
        ):
            violations.append(gate["output"])

    violations.sort()

    return ",".join(violations)


def main() -> None:
    ans = get_ans()
    print(ans)


if __name__ == "__main__":
    main()
