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


def get_corners(coords: list[tuple[int, int]], regions: dict, key: str) -> int:
    # Putting comments here in case I forget, which is 99% the case
    # This adds corner points to the coord in `coords`
    adds = [
        (0, 0), (0, 1),
        (1, 0), (1, 1),
    ]

    corners = {}

    # Generate the coords for the corners
    for coord in coords:
        for add in adds:
            corner = coord[0] + add[0], coord[1] + add[1]
            if corner not in corners:
                corners[corner] = 1
            else:
                corners[corner] += 1


    filtered_regions = {k: v for k, v in regions.items() if k != key}

    # This adds corner points to corners
    # Meaning the "corner points" are now the actual coords of a plant
    corner_adds = [
        (-1, -1), (-1, 0),
        (0, -1), (0, 0)
    ]

    # In case a "corner point" is shared diagonally between different regions
    diagonal_patterns = [
        [
            (True, False),
            (False, True),
            (False, True),
            (True, False),
        ],
        [
            (False, True),
            (True, False),
            (True, False),
            (False, True),
        ],
    ]

    total = 0

    for k, v in corners.items():
        # Odd corners are immediately a corner of the overall region
        if v % 2 != 0:
            total += 1
        # If a corner has a value of two, it is shared on other plants
        # We need to find if these corners of a plant are diagonally shared
        elif v == 2:
            observed_pattern = []

            for add in corner_adds:
                # This "corner" is now a coord of a plant in any region
                # Or outside the map
                c = k[0] + add[0], k[1] + add[1]
                # Break if out of bounds
                if c[0] < 0 or c[1] < 0:
                    break

                # If the added corner is in the region
                exist_in_key = c in coords
                # Checks if a corner is present in any region other than the current one
                exist_in_other_regions = any(
                    c in region
                    for regions_by_key in filtered_regions.values()
                    for region in regions_by_key.values()
                )

                observed_pattern.append((exist_in_key, exist_in_other_regions))
                # Check if it follows the diagonal pattern and add it to the total
                for pattern in diagonal_patterns:
                    if observed_pattern[-len(pattern):] == pattern:
                        total += v
                        break

    return total


def get_sides(regions: dict) -> dict:
    sides = {}

    for key, value in regions.items():
        for k, v in value.items():
            corners = get_corners(v, regions, key)

            if key not in sides:
                sides[key] = {
                    k: corners
                }
            else:
                sides[key][k] = corners

    return sides



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
    sides = get_sides(regions)
    total = get_fence_cost(areas, sides)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
