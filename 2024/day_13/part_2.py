def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_machines(lines: list[str]) -> list[list[str]]:
    split_lists = []
    current_list = []

    for item in lines:
        if item == "":
            if current_list:
                split_lists.append(current_list)
                current_list = []
        else:
            current_list.append(item)

    if current_list:
        split_lists.append(current_list)

    return split_lists


def print_machines(machines: list[list[str]]) -> None:
    for machine in machines:
        print(machine)


def parse_machine(machine: list[str]) -> dict:
    coordinates = {}
    add = 10_000_000_000_000

    for item in machine:
        key, value = item.split(": ")
        x, y = value.replace("X", "").replace("Y", "").replace("+", "").replace("=", "").split(", ")
        if key == "Prize":
            coordinates[key] = (int(x) + add, int(y) + add)
        else:
            coordinates[key] = (int(x), int(y))

    return coordinates

def get_tokens(machine: list[str]) -> int:
    button_costs = (3, 1)
    coords = parse_machine(machine)
    a, b, prize = coords["Button A"], coords["Button B"], coords["Prize"]

    i = ( (b[1] * prize[0]) - (b[0] * prize[1]) ) / ( (a[0] * b[1]) - (a[1] * b[0]) )
    j = ( prize[1] - i * a[1] ) / b[1]
    
    if i == int(i) and j == int(j):
        return int(i * button_costs[0] + j * button_costs[1])

    return 0


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    machines = get_machines(lines)

    total = 0

    for machine in machines:
        total += get_tokens(machine)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
