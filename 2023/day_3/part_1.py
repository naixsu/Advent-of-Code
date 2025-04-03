def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


# Debug function
def print_lines(lines: list[list[str]]) -> None:
    for line in lines:
        print(''.join(str(line)))


def in_bounds(grid_size: tuple[int, int], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < grid_size[0] and 0 <= coords[1] < grid_size[1]


def get_full_number(grid: list[list[str]], row: int, col: int, visited: set) -> int:
    if not grid[row][col].isdigit() or (row, col) in visited:
        return 0

    visited.add((row, col))

    start, end = col, col

    # Check to the left
    while start > 0 and grid[row][start - 1].isdigit():
        visited.add((row, start - 1))
        start -= 1

    # Check to the right
    while end < len(grid[row]) - 1 and grid[row][end + 1].isdigit():
        visited.add((row, end + 1))
        end += 1

    return int(''.join(grid[row][start:end + 1]))


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    lines = [list(line) for line in lines]
    grid_size = len(lines), len(lines[0])

    moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]
    total = 0

    visited = set()

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            # If current char is not a digit or '.'
            if char.isdigit() or char == ".":
                continue

            for dx, dy in moves:
                new_row = row + dy
                new_col = col + dx

                if not in_bounds(grid_size, (new_row, new_col)):
                    continue

                number = get_full_number(lines, new_row, new_col, visited)
                total += number

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
