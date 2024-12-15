def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def setup(lines: list[list[str]]) -> dict:
    freqs = {}

    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char == ".":
                continue
            if char not in freqs:
                freqs[char] = [(j, i)]
            else:
                freqs[char].append((j, i))

    return freqs


def in_bounds(grid_size: tuple[int, int], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < grid_size[0] and 0 <= coords[1] < grid_size[1]


def get_link_dist(p1, p2):
    d1 = -(p1[0] - p2[0])
    d2 = -(p1[1] - p2[1])

    return (d1, d2)


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    lines = [list(line) for line in lines]
    grid_size = len(lines[0]), len(lines)

    freqs = setup(lines)
    antinodes = set()

    for values in freqs.values():
        for i, value in enumerate(values):
            for j, val in enumerate(values):
                if i == j:
                    continue
                dist = get_link_dist(value, val)
                new = val[0] + dist[0], val[1] + dist[1]
                if in_bounds(grid_size, new):
                    antinodes.add(new)

    return len(antinodes)


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
