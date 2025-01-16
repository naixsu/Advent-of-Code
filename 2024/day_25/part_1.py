def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def group_input(lines: list[str]) -> tuple[dict, dict]:
    groups, current_group = [], []

    for line in lines:
        if line == "":
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(line)

    if current_group:
        groups.append(current_group)

    return groups


def init(groups: list[list[str]]) -> tuple[list, list]:

    locks, keys = [], []
    lock = True
    # The locks are schematics that have the top row filled (#) and the bottom row empty (.);

    for group in groups:
        start, end = group[0], group[-1]
        heights = [0] * 5

        if start.count("#") == 5 and end.count(".") == 5:
            lock = True

        if start.count(".") == 5 and end.count("#") == 5:
            lock = False

        pins = group[1:-1]

        for pin in pins:
            for i, p in enumerate(pin):
                heights[i] += p.count("#")

        if lock:
            locks.append(heights)
        else:
            keys.append(heights)

    return locks, keys


def is_overlap(lock: dict, key: dict) -> bool:
    max_sum = 5
    overlap = any(a + b > max_sum for a, b in zip(lock, key))

    return overlap


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    total = 0
    groups = group_input(lines)
    locks, keys = init(groups)

    for i, lock in enumerate(locks):
        for j, key in enumerate(keys):
            if not is_overlap(lock, key):
                total += 1

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
