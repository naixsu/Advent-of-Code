def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def in_bounds(grid_size: tuple[int, int], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < grid_size[0] and 0 <= coords[1] < grid_size[1]


def get_total_seen(lines: list[str], grid_size: tuple[int, int], row: int, col: int) -> int:
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

        if lines[new_row][new_col] == "@":
            seen.append((new_row, new_col))


    return len(seen)


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    grid_size = len(lines), len(lines[0])

    total = 0

    for row, line in enumerate(lines):
        for col, char in enumerate(line):

            if char != "@":
                continue

            if get_total_seen(lines, grid_size, row, col) < 4:
                total += 1

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
