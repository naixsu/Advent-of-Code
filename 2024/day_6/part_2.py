def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_guard_index(lines: list[list[str]], direction: str) -> tuple[tuple[int, int, int]]:
    dir_num = {
        "^": 0,
        ">": 1,
        "v": 2,
        "<": 3,
    }

    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char in dir_num:
                return (j, i, dir_num[direction])


def in_bounds(grid_size: tuple[int, int], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < grid_size[0] and 0 <= coords[1] < grid_size[1]


def print_lines(lines: list[list[str]]) -> None:
    for line in lines:
        print(line)


def is_loop(grid_size: tuple[int, int], curr: tuple[int, int], lines: list[list[str]]) -> bool:
    # This function is quite similar to `get_original_path()` but I'm too lazy to generalize them
    # Up: 0, Right: 1, Down: 2, Left: 3
    moves = {
        # Invert X Y
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1),
    }

    visited = {}

    while in_bounds(grid_size, curr[:2]):
        visited[curr] = visited.get(curr, 0) + 1
        if visited[curr] > 2:
            return True

        direction = curr[2]
        add = moves[direction]
        next = curr[0] + add[0], curr[1] + add[1], direction

        if not in_bounds(grid_size, next[:2]):
            break

        if lines[next[0]][next[1]] == "#" or lines[next[0]][next[1]] == "O":
            curr = curr[0], curr[1], (direction + 1) % 4
            continue

        curr = next

    return False


def get_original_path(grid_size: tuple[int, int], curr: tuple[int, int], lines: list[list[str]]) -> list[tuple[int, int]]:
    # This function is quite similar to `is_loop()` but I'm too lazy to generalize them
    moves = {
        # Invert X Y
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1),
    }

    visited = []

    while in_bounds(grid_size, (curr[0], curr[1])):
        if (curr[:2]) not in visited:
            visited.append(curr[:2])

        direction = curr[2]
        add = moves[direction]
        next = curr[0] + add[0], curr[1] + add[1], direction

        if not in_bounds(grid_size, next[:2]):
            break

        if lines[next[0]][next[1]] == "#":
            curr = curr[0], curr[1], (direction + 1) % 4
            continue

        curr = next

    return visited


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    lines = [list(line) for line in lines]
    grid_size = len(lines[0]), len(lines)

    # Invert row and col
    curr = get_guard_index(lines, "^")
    
    original_path = get_original_path(grid_size, curr, lines)

    total = 0

    for index, path in enumerate(original_path):
        lines[path[0]][path[1]] = "O"
        
        print("Checking path", index, path)

        if is_loop(grid_size, curr, lines):
            total += 1
        
        lines[path[0]][path[1]] = "."

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
