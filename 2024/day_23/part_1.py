def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def init_computers(lines: list[str]) -> set:
    return set(lines)


def get_connections(lines: list[str]) -> dict:
    connections = {}

    for line in lines:
        first, second = line.split("-")
        connections.setdefault(first, set()).add(second)
        connections.setdefault(second, set()).add(first)

    return connections


def get_connected_computers(computers: set, connections: dict, starting_name: str) -> set:
    connected_computers = set()

    for computer in computers:
        first, second = computer.split("-")

        # Modifying `computers` while iterating might be bad but eh whatever
        # We added it back in anyways. Should be fine I think. 
        computers.remove(computer)

        for comp in computers:
            connected = False
            l, r = comp.split("-")

            connected = (
                (l == first and r in connections[second]) or
                (r == second and l in connections[first]) or
                (l == second and r in connections[first]) or
                (r == first and l in connections[second])
            )

            if connected:
                connection = sorted({first, second, l, r})

                if any(con.startswith(starting_name) for con in connection):
                    connection = ",".join(connection)
                    connected_computers.add(connection)

        computers.add(computer)

    return connected_computers


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    starting_name = "t"
    computers = init_computers(lines)
    connections = get_connections(lines)
    connected_computers = get_connected_computers(computers, connections, starting_name)

    total = len(connected_computers)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
