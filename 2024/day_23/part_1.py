def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_connections(lines: list[str]) -> dict:
    connections = {}

    for line in lines:
        first, second = line.split("-")
        connections.setdefault(first, []).append(second)
        connections.setdefault(second, []).append(first)

    return connections


def get_connected_computers(connections: dict, starting_name: str) -> set:
    connected_computers = set()

    for comp, cons in connections.items():
        for i in range(len(cons) - 1):
            for j in range(i + 1, len(cons)):

                if cons[j] in connections[cons[i]] and comp in connections[cons[j]]:
                    connection = sorted([comp, cons[i], cons[j]])

                    if any(con.startswith(starting_name) for con in connection):
                        connection = ",".join(connection)
                        connected_computers.add(connection)

    return connected_computers


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    starting_name = "t"
    connections = get_connections(lines)
    connected_computers = get_connected_computers(connections, starting_name)

    total = len(connected_computers)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
