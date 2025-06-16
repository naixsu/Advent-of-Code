def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_nodes(lines: list[str]) -> dict:
    nodes = {}

    for line in lines:
        line = line.split()
        tup = (line[2][1:4], line[3][0:3])
        nodes[line[0]] = tup

    return nodes


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    instructions = lines.pop(0)
    lines.pop(0)

    nodes = get_nodes(lines)

    node = "AAA"
    i = 0

    while node != "ZZZ":
        direction = instructions[i % len(instructions)]
        direction = 0 if direction == "L" else 1
        next_node = nodes[node][direction]
        node = next_node

        i += 1

    return i


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
