def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def print_lines(lines: list[list[str]]) -> None:
    for line in lines:
        print(''.join(str(line)))


def in_bounds(grid_size: tuple[int, int], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < grid_size[0] and 0 <= coords[1] < grid_size[1]


def find_trailheads(lines: list[list[int]]) -> tuple[int, int]:
    trailheads = []

    for j, line in enumerate(lines):
        for i, num in enumerate(line):
            if num == 0:
                trailheads.append((j, i))

    return trailheads


def bfs_count_paths(grid_size: tuple[int, int], lines: list[list[int]], start: tuple[int, int]) -> int:
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = [start]
    visited = set()
    count = 0

    while queue:
        current = queue.pop(0)

        if current in visited:
            continue

        visited.add(current)
        x, y = current

        if lines[x][y] == 9:
            count += 1
            continue

        for dx, dy in moves:
            next_pos = (x + dx, y + dy)

            if in_bounds(grid_size, next_pos):
                nx, ny = next_pos

                if next_pos not in visited and lines[nx][ny] == lines[x][y] + 1:
                    queue.append(next_pos)

    return count


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).strip().split("\n")
    lines = [list(map(int, line)) for line in lines]
    grid_size = len(lines), len(lines[0])
    trailheads = find_trailheads(lines)
    total = 0

    for trailhead in trailheads:
        total += bfs_count_paths(grid_size, lines, trailhead)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
