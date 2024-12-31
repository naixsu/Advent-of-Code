def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def print_lines(lines: list[list[str]]) -> None:
    for line in lines:
        print("".join(line))


def get_maze_hash(lines: list[list[str]]) -> dict:
    maze_hash = {}

    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char not in maze_hash:
                maze_hash[char] = [(j, i)]
            else:
                maze_hash[char].append((j, i))

    return maze_hash


def get_neighbors(position: tuple[int, int], current_direction: str, maze_hash: dict) -> list[tuple[int, int], str, int]:
    directions = {
        "north": (-1, 0),
        "south": (1, 0),
        "west": (0, -1),
        "east": (0, 1),
    }
    neighbors = []
    walls = maze_hash["#"]
    end = maze_hash["E"]

    for new_direction, (dx, dy) in directions.items():
        nx, ny = position[0] + dx, position[1] + dy
        if (nx, ny) not in walls or (nx, ny) == end:
            rotation_cost = 1000 if new_direction != current_direction else 0
            neighbors.append(((nx, ny), new_direction, rotation_cost))

    return neighbors


def get_shortest_path(maze_hash: dict) -> int:
    start = maze_hash['S'][0]
    end = maze_hash['E'][0]

    # Priority queue with (current_distance, current_position, current_direction, path)
    prio = [(0, start, "east")]  # Start moving east
    distances = {(start, "east"): 0}
    visited = set()

    while prio:
        # Get the current node
        current_distance, current_position, current_direction = min(
            prio, key=lambda x: x[0]
        )
        prio.remove((current_distance, current_position, current_direction))
        visited.add((current_position, current_direction))

        if current_position == end:
            return current_distance

        for neighbor, new_direction, rotation_cost in get_neighbors(
            current_position, current_direction, maze_hash
        ):
            if (neighbor, new_direction) in visited:
                continue

            new_distance = current_distance + 1 + rotation_cost

            if (neighbor, new_direction) not in distances or new_distance < distances[
                (neighbor, new_direction)
            ]:
                distances[(neighbor, new_direction)] = new_distance
                prio.append((new_distance, neighbor, new_direction))

    return float('inf') # No path found

def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    maze_hash = get_maze_hash(lines)

    shortest_path = get_shortest_path(maze_hash)
    return shortest_path


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
