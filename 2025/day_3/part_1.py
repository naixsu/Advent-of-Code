def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def largest_two_digit_subnumber(digits: list[int]) -> int:
    best = -1
    n = len(digits)

    for i in range(n - 1):
        first = digits[i]
        second = max(digits[i + 1:])
        best = max(best, first * 10 + second)

    return best


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    total = 0

    for line in lines:
        digits = list(map(int, line))
        max_num = largest_two_digit_subnumber(digits)
        total += max_num

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
