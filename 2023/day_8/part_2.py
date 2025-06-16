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


def get_starting_nodes(dict) -> list[dict]:
    starting_nodes = []

    for key in dict.keys():
        if key[-1] == "A":
            starting_nodes.append(key)

    return starting_nodes


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def lcm_list(numbers: list[int]) -> int:
    result = numbers[0]

    for number in numbers[1:]:
        result = lcm(result, number)

    return result


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    instructions = lines.pop(0)
    lines.pop(0)

    nodes = get_nodes(lines)
    starting_nodes = get_starting_nodes(nodes)

    def get_cycle_length(start_node: str) -> int:
        i = 0
        curr = start_node

        while True:
            if curr[-1] == "Z":
                return i

            direction = instructions[i % len(instructions)]
            direction = 0 if direction == "L" else 1
            curr = nodes[curr][direction]
            i += 1

    cycle_lengths = [get_cycle_length(node) for node in starting_nodes]

    return lcm_list(cycle_lengths)


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
