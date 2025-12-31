def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def in_bounds(grid_size: tuple[int, int], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < grid_size[0] and 0 <= coords[1] < grid_size[1]


def get_total_seen(lines: list[str], grid_size: tuple[int, int], row: int, col: int, big_seen: list[tuple[int, int]]) -> int:
    seen = []
    moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    for dx, dy in moves:
        new_row = row + dy
        new_col = col + dx

        if not in_bounds(grid_size, (new_row, new_col)):
            continue

        if lines[new_row][new_col] == "@" and (new_row, new_col) not in big_seen:
            seen.append((new_row, new_col))


    return len(seen)


def get_total(lines: list[str], grid_size: tuple[int, int]) -> int:
    total = 0
    big_seen = set()

    # collect all @ positions once
    active = {
        (r, c)
        for r, line in enumerate(lines)
        for c, ch in enumerate(line)
        if ch == "@"
    }

    while True:
        small_seen = set()

        for row, col in active:
            if (row, col) in big_seen:
                continue

            if get_total_seen(lines, grid_size, row, col, big_seen) < 4:
                small_seen.add((row, col))

        if not small_seen:
            break

        total += len(small_seen)
        big_seen |= small_seen
        active -= small_seen

    return total


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    grid_size = len(lines), len(lines[0])

    return get_total(lines, grid_size)


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    grid_size = len(lines), len(lines[0])

    total = get_total(lines, grid_size)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
