def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_ids(lines: list[str]) -> list[str]:
    # Acc to the problem, we are expecting a single line
    return lines[0].split(",")


def get_number_of_digits(num: str) -> int:
    return len(num)


def is_even_digits(num: str) -> bool:
    return get_number_of_digits(num) % 2 == 0


def is_invalid(num: str) -> bool:
    length = len(num)
    mid = length // 2

    return num[0:mid] == num[mid:length]

def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    ids = get_ids(lines)

    total = 0

    for id in ids:
        first, last = id.split("-")

        for num in range(int(first), int(last) + 1):
            if not is_even_digits(str(num)):
                continue

            if is_invalid(str(num)):
                total += num

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
