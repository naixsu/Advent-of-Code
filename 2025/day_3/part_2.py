def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def largest_k_digit_subnumber(digits: list[int], k: int) -> int:
    result = []
    start = 0
    n = len(digits)

    for remaining in range(k, 0, -1):
        end = n - remaining + 1

        max_digit = -1
        max_index = -1

        for i in range(start, end):
            if digits[i] > max_digit:
                max_digit = digits[i]
                max_index = i

        result.append(max_digit)
        start = max_index + 1

    num = 0

    for d in result:
        num = num * 10 + d

    return num


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    total = 0

    for line in lines:
        digits = list(map(int, line))
        max_num = largest_k_digit_subnumber(digits, 12)
        total += max_num

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
