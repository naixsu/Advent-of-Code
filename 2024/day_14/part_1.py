def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_robots(lines: list[str]) -> list[list[tuple[int, int]]]:
    robots = []

    for line in lines:
        robot = line.replace("p", "").replace("v", "").replace("=", "").split(" ")
        pos = tuple(map(int, robot[0].split(",")))
        vel = tuple(map(int, robot[1].split(",")))

        robots.append([pos, vel])

    return robots


def get_safety_factor(
    robots: list[list[tuple[int, int]]],
    grid_size: tuple[int, int],
    seconds: int
) -> int:

    width, height = grid_size
    mid_w, mid_h = width // 2, height // 2
    q1, q2, q3, q4 = 0, 0, 0, 0

    for robot in robots:
        pos, vel = robot
        x = (pos[0] + (seconds * vel[0])) % width
        y = (pos[1] + (seconds * vel[1])) % height

        if x == mid_w or y == mid_h:
            continue

        if x > mid_w and y < mid_h:
            q1 += 1
        elif x < mid_w and y < mid_h:
            q2 += 1
        elif x < mid_w and y > mid_h:
            q3 += 1
        else:
            q4 += 1

    total = q1 * q2 * q3 * q4

    return total


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    robots = get_robots(lines)
    seconds = 100
    width, height = 101, 103

    total = get_safety_factor(robots, (width, height), seconds)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
