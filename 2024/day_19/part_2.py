def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def count_ways(design: str, towels: dict) -> int:
    memo = {}

    def dp(start: int) -> int:
        if start == len(design):
            return 1

        if start in memo:
            return memo[start]

        total_ways = 0

        for pattern in towels:
            if design.startswith(pattern, start):
                total_ways += dp(start + len(pattern))

        memo[start] = total_ways

        return total_ways

    return dp(0)


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    towels = set(lines[0].split(", "))
    designs = lines[2:]
    total = 0

    for design in designs:
        total += count_ways(design, towels)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
