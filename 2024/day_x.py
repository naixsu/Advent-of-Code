def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    total = 0

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
