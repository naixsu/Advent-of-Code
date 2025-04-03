def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    total = 0

    for i, line in enumerate(lines):
        line = line.split("|")
        winning = line[0]
        winning = winning.split(":")[1].strip(" ").split(" ")
        winning = [num for num in winning if num != ""]
        winning = set(map(int, winning))

        mine = line[1]
        mine = mine.strip(" ").split(" ")
        mine = [num for num in mine if num != ""]
        mine = map(int, mine)

        count = sum(1 for num in mine if num in winning)

        if count > 2:
            total += 2 ** (count - 1)
        else:
            total += count

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
