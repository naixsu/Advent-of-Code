import re

def read_from_file(file_name: str) -> str:
    lines = []
    with open(file_name, "r") as file:
        for line in file:
            lines.append(line.rstrip())

    return lines


def parse_line(line: str) -> list[str]:
    pattern = r"mul\(\d+,\d+\)"
    matched = re.findall(pattern, line)

    return matched


def evaluate_expressions(expressions: list[str]) -> int:
    sum = 0
    pattern = r"mul\((\d+),(\d+)\)"

    for expr in expressions:
        numbers = re.findall(pattern, expr)
        numbers = tuple(map(int, numbers[0]))
        
        sum += numbers[0] * numbers[1]
    
    return sum


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name)
    sum = 0

    for line in lines:
        expressions = parse_line(line)
        sum += evaluate_expressions(expressions)

    return sum


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
