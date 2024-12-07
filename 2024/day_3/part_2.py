import re

def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def parse_line(line: str) -> list[str]:
    pattern = r"don't\(\).*?(?=do\(\)|$)"

    # Use re.sub() to remove everything between "don't()" and "do()"
    result = re.sub(pattern, "", line, flags=re.DOTALL)
    pattern = r"mul\(\d+,\d+\)"
    matched = re.findall(pattern, result)

    return matched


def evaluate_expressions(expressions: str) -> int:
    sum = 0
    pattern = r"\d+"
    
    for expr in expressions:
        numbers = re.findall(pattern, expr)
        numbers = tuple(map(int, numbers))
        sum += numbers[0] * numbers[1]

    return sum


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name)

    expressions = parse_line(lines)
    sum = evaluate_expressions(expressions)

    return sum


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
