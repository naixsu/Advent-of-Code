import math

def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_ids(lines: list[str]) -> list[str]:
    # Acc to the problem, we are expecting a single line
    return lines[0].split(",")


def is_even_digits(num: str) -> bool:
    return len(num) % 2 == 0


def is_invalid(num: str) -> bool:
    n = len(num)

    if n <= 1:
        return False

    for block_size in range(1, n // 2 + 1):
        if n % block_size != 0:
            continue

        block = num[:block_size]
        repeats = n // block_size

        if block * repeats == num:
            return True

    return False


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    ids = get_ids(lines)

    total = 0

    for id in ids:
        first, last = id.split("-")

        for num in range(int(first), int(last) + 1):
            if is_invalid(str(num)):
                total += num

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
