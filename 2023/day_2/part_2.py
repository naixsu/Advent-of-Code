def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    colors = {
        "red": 0, "green": 0, "blue": 0,
    }
    total = 0

    for line in lines:
        line = line.split(" ")

        for i, char in enumerate(line):
            char = char.strip(":,;")

            if char in colors:
                colors[char] = max(
                    int(line[i - 1]),
                    colors[char]
                )

        total += colors["red"] * colors["green"] * colors["blue"]

        colors = {
            "red": 0, "green": 0, "blue": 0,
        } 

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
