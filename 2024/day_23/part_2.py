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


def is_clique(subset: list[str], connections: dict) -> bool:
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):

            if subset[j] not in connections[subset[i]]:
                return False

    return True


def generate_subsets(cons: list[str], size: int) -> list[str]:
    if size == 0:
        return [[]]
    if len(cons) < size:
        return []

    subsets = []

    for i in range(len(cons)):
        rest_subsets = generate_subsets(cons[i + 1:], size - 1)

        for subset in rest_subsets:
            subsets.append([cons[i]] + subset)

    return subsets


def get_connected_computers(connections: dict) -> str:
    connected_computers = []

    for comp, cons in connections.items():
        for i in range(len(cons), 1, -1):

            if i < len(connected_computers):
                break

            subsets = generate_subsets(cons, i)

            for subset in subsets:
                if is_clique(subset, connections):
                    clique = sorted(subset + [comp])
                    connected_computers.append(clique)
                    break

    max_length_connected_computers = max(connected_computers, key=len)

    return ",".join(max_length_connected_computers)


def get_ans() -> str:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    connections = get_connections(lines)
    connected_computers = get_connected_computers(connections)

    return connected_computers


def main() -> None:
    ans = get_ans()
    print(ans)


if __name__ == "__main__":
    main()
