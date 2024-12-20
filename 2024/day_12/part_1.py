def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def print_lines(lines: list[list[str]]) -> None:
    for line in lines:
        print(line)


def in_bounds(grid_size: tuple[int, int], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < grid_size[0] and 0 <= coords[1] < grid_size[1]


def get_regions(lines: list[list[str]]) -> dict:
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    grid_size = len(lines), len(lines[0])
    visited = set()
    regions = {}

    def _bfs(start: tuple[int, int], char: str) -> list[tuple[int, int]]:
        queue = [start]
        group = []

        while queue:
            curr = queue.pop(0)
            if curr in visited:
                continue
            visited.add(curr)
            group.append(curr)

            for move in moves:
                next = curr[0] + move[0], curr[1] + move[1]
                if in_bounds(grid_size, next) and next not in visited and lines[next[0]][next[1]] == char:
                    queue.append(next)

        return group

    for j in range(grid_size[0]):
        for i in range(grid_size[1]):
            coord = (j, i)
            if coord not in visited:
                char = lines[j][i]
                group = _bfs(coord, char)
                if char not in regions:
                    regions[char] = {1: group}
                else:
                    group_number = len(regions[char]) + 1
                    regions[char][group_number] = group

    return regions


def get_areas(regions: dict) -> dict:
    areas = {}

    for key, value in regions.items():
        for k, v in value.items():
            if key not in areas:
                areas[key] = {
                    k: len(v)
                }
            else:
                areas[key][k] = len(v)

    return areas


def get_perimeters(regions: dict) -> dict:
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    perimeters = {}

    for key, value in regions.items():
        for k, v in value.items():
            perimeter = 0

            for coords in v:
                for move in moves:
                    next = coords[0] + move[0], coords[1] + move[1]
                    if next not in v:
                        perimeter += 1

            if key not in perimeters:
                perimeters[key] = {
                    k: perimeter
                }
            else:
                perimeters[key][k] = perimeter


    return perimeters


def get_fence_cost(areas: dict, perimeters: dict) -> int:
    total = 0

    cost = {}
    for key in areas:
        if key in perimeters:
            cost[key] = {
                subkey: areas[key][subkey] * perimeters[key].get(subkey, 1)
                for subkey in areas[key]
            }

            total += sum(cost[key].values())

    return total


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).strip().split("\n")
    lines = [line for line in lines]

    total = 0

    regions = get_regions(lines)
    areas = get_areas(regions)
    perimeters = get_perimeters(regions)
    total = get_fence_cost(areas, perimeters)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
