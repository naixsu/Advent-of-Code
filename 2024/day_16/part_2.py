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


def get_shortest_paths(maze_hash: dict) -> tuple[int, list[list[tuple[int, int]]]]:
    start = maze_hash["S"][0]
    end = maze_hash["E"][0]

    # Priority queue with (current_distance, current_position, current_direction, path)
    prio = [(0, start, "east", [start])]
    distances = {(start, "east"): 0}
    visited = set()
    paths = []

    shortest_distance = float('inf')

    while prio:
        print(len(prio)) # Putting this as a debugger because this took forever to run
        # Get the current node with the smallest distance
        current_distance, current_position, current_direction, path = min(
            prio, key=lambda x: x[0]
        )
        prio.remove((current_distance, current_position, current_direction, path))
        visited.add((current_position, current_direction))

        if current_position == end:
            if current_distance == shortest_distance:
                paths.append(path)
            elif current_distance < shortest_distance:
                shortest_distance = current_distance
                paths = [path]
            continue

        for neighbor, new_direction, rotation_cost in get_neighbors(
            current_position, current_direction, maze_hash
        ):
            if (neighbor, new_direction) in visited:
                continue

            new_distance = current_distance + 1 + rotation_cost
            new_path = path + [neighbor]

            # Check if we have found a shorter or equally short path
            if (neighbor, new_direction) not in distances or new_distance < distances[
                (neighbor, new_direction)
            ]:
                distances[(neighbor, new_direction)] = new_distance
                prio.append((new_distance, neighbor, new_direction, new_path))

            # If this is an equal distance, we add the path to prio without updating distances
            elif new_distance == distances.get((neighbor, new_direction), float('inf')):
                prio.append((new_distance, neighbor, new_direction, new_path))

    return shortest_distance, paths


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    maze_hash = get_maze_hash(lines)
    shortest_distance, paths = get_shortest_paths(maze_hash)
    paths = {node for path in paths for node in path}
    tiles = len(paths)

    return tiles


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
