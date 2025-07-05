from collections import deque

def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def in_bounds(grid_size: tuple[int, int], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < grid_size[0] and 0 <= coords[1] < grid_size[1]


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    lines = [list(line) for line in lines]
    grid_size = len(lines), len(lines[0])
    moves = {
        "N": (-1, 0), "S": (1, 0),
        "E": (0, 1), "W": (0, -1)
    }

    pipes = {
        "|": "NS", "-": "EW", "L": "NE",
        "J": "NW", "7": "SW", "F": "SE",
        "S": "NSEW"
    }

    start = None
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "S":
                start = (row, col)
                break

    # Figure out what pipe start is
    # TODO:
    # THIS IS HARDCODED.
    # FIGURE OUT HOW TO FIGURE OUT THE START PIPE
    # CLEAN THIS UP I GUESS
    lines[start[0]][start[1]] = "-"

    def bfs(start):
        queue = deque([start])
        visited = set([start])
        steps = -1

        while queue:
            steps += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                if lines[x][y] not in pipes:
                    continue

                dirs = list(pipes[lines[x][y]])

                for move in dirs:
                    dx, dy = moves[move]
                    nx, ny = x + dx, y + dy

                    if (
                        in_bounds(grid_size, (nx, ny)) and
                        (nx, ny) not in visited and
                        lines[nx][ny] != "."
                    ):
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        return steps

    total = bfs(start)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
