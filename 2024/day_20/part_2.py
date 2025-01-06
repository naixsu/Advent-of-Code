def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_path(start: tuple[int, int], end: tuple[int, int], walls: set) -> dict:
    queue = [(start, 0)]
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    visited_with_steps = {}

    while queue:
        curr, steps = queue.pop(0)

        if curr in visited:
            continue
        
        visited.add(curr)
        visited_with_steps[curr] = steps

        if curr == end:
            return visited_with_steps

        y, x = curr

        for dy, dx in moves:
            next_pos = (y + dy, x + dx)

            if (
                next_pos not in visited
                and next_pos not in walls
            ):
                queue.append((next_pos, steps + 1))

    return visited_with_steps


def get_path_with_cheats(path: dict, end: tuple[int, int], max_cheat_cost: int) -> dict:
    cheat_freq = {}

    for coord, steps in path.items():
        y, x = coord

        if coord == end:
            break

        for dy in range(-max_cheat_cost, max_cheat_cost + 1):
            for dx in range(-max_cheat_cost, max_cheat_cost + 1):
                if abs(dy) + abs(dx) > max_cheat_cost or (dy == 0 and dx == 0):
                    continue

                next_pos = (y + dy, x + dx)
                cheat_cost = abs(dy) + abs(dx)

                if (
                    next_pos in path
                    and path[next_pos] > steps + cheat_cost
                ):
                    saved_picoseconds = path[next_pos] - (steps + cheat_cost)

                    if saved_picoseconds not in cheat_freq:
                        cheat_freq[saved_picoseconds] = 1
                    else:
                        cheat_freq[saved_picoseconds] += 1

    return cheat_freq


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    lines = [list(line) for line in lines]
    start, end, walls, cells = None, None, set(), set()
    total = 0
    max_cheat_cost = 20

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                start = (y, x)
            elif char == "E":
                end = (y, x)
            elif char == "#":
                walls.add((y, x))
            elif char == ".":
                cells.add((y, x))

    path = get_path(start, end, walls)
    path_with_cheats = get_path_with_cheats(path, end, max_cheat_cost)

    for picoseconds, cheat_freq in path_with_cheats.items():
        if picoseconds >= 100:
            total += cheat_freq

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
