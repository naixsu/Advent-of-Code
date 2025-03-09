def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_valid_game(line: str) -> int:
    line = line.split(" ")
    RED, GREEN, BLUE = 12, 13, 14
    colors = {
        "red": RED, "green": GREEN, "blue": BLUE,
    }
    id = 0

    def is_not_valid_colors() -> bool:
        return (
            colors["red"] < 0 or
            colors["green"] < 0 or
            colors["blue"] < 0
        ) 

    for i, char in enumerate(line):
        char = char.strip(":,")
        end = False
        if i == 1:
            id = int(char)

        if char.isdigit() and i > 1:
            next = line[i + 1].strip(",")

            if ";" in next:
                end = True
                next = next.strip(";")

            colors[next] -= int(char)

            if end:
                end = False

                if is_not_valid_colors():
                    return 0

                colors["red"] = RED
                colors["green"] = GREEN
                colors["blue"] = BLUE

    if is_not_valid_colors():
        return 0

    return id


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    total = 0

    for line in lines:
        total += get_valid_game(line)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
