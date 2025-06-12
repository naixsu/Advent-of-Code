def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    time = int(''.join(lines[0].split(":")[1].split()))
    dist = int(''.join(lines[1].split(":")[1].split()))

    total = 0

    for t in range(1, time):
        if (time - t) * t > dist:
            total += 1

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()

