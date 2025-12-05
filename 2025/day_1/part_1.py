def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_rotations(lines: list[str]) -> list[tuple[str, int]]:
    rotations = []

    for line in lines:
        direction = line[0]
        dials = int(line[1:])

        rotations.append((direction, dials))

    return rotations


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    rotations = get_rotations(lines)

    total = 0
    start = 50
    curr = start

    for rotation in rotations:
        direction = rotation[0]
        dials = rotation[1]

        if direction == "L":
            curr = (curr - dials) % 100
        else:
            curr = (curr + dials) % 100

        if curr == 0:
            total += 1

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()


