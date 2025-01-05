def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def is_valid_design(design: str, towels: dict) -> bool:
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):

            if dp[j] and design[j:i] in towels:
                dp[i] = True
                break

    return dp[n]


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    towels = set(lines[0].split(", "))
    designs = lines[2:]
    total = 0

    for design in designs:
        if is_valid_design(design, towels):
            total += 1

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
