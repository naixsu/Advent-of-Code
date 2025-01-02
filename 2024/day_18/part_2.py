def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()
    return line


def in_bounds(grid_size: tuple[int, int], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < grid_size[0] and 0 <= coords[1] < grid_size[1]


def get_steps(byte_positions: set[tuple[int, int]], grid_size: tuple[int, int]) -> tuple[int, set]:
    start = (0, 0)
    end = (grid_size[0], grid_size[1])
    expanded_grid_size = (grid_size[0] + 1, grid_size[1] + 1)
    queue = [(start, 0)]
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    visited.add(start)

    while queue:
        curr, steps = queue.pop(0)

        if curr == end:
            return steps, visited

        y, x = curr

        for dy, dx in moves:
            next_pos = (y + dy, x + dx)

            if (
                in_bounds(expanded_grid_size, next_pos)
                and next_pos not in visited
                and next_pos not in byte_positions
            ):
                visited.add(next_pos)
                queue.append((next_pos, steps + 1))

    return -1, visited


def init_byte_positions(lines: list[str]) -> list[tuple[int, int]]:
    byte_positions = []

    for line in lines:
        x, y = map(int, line.split(","))
        byte_positions.append((y, x))

    return byte_positions


def get_cut_off() -> str:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    byte_positions = init_byte_positions(lines)
    stop = 1024
    initial_positions = set(byte_positions[:stop])
    remaining_bytes = byte_positions[stop:]
    grid_size = (70, 70)

    for byte_pos in remaining_bytes:
        initial_positions.add(byte_pos)
        steps, _ = get_steps(initial_positions, grid_size)

        if steps == -1:
            return f"{byte_pos[1]},{byte_pos[0]}"

    return "No cut-off found"


def main() -> None:
    cut_off = get_cut_off()
    print(cut_off)


if __name__ == "__main__":
    main()
