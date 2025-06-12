def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    times = list(map(int, lines[0].split(":")[1].split()))
    dists = list(map(int, lines[1].split(":")[1].split()))

    races = list(zip(times, dists))
    total = 1

    for time, dist in races:
        rec = 0

        for t in range(1, time):
            if (time - t) * t > dist:
                rec += 1

        total *= rec


    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()

