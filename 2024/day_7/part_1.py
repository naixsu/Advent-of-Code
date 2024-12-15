def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def evaluate_left_to_right(expression: str) -> int:
    tokens = expression.split()
    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        number = int(tokens[i + 1])
        
        if operator == "+":
            result += number
        elif operator == "*":
            result *= number

    return result


def generate_combinations(target: int, numbers: list[int], index=0, current="") -> bool:
    operators = ["+", "*"]

    if index == len(numbers) - 1:
        val = current + str(numbers[index])
        res = evaluate_left_to_right(val)

        return res == target

    for op in operators:
        next_expression = current + str(numbers[index]) + f" {op} "
        if generate_combinations(target, numbers, index + 1, next_expression):
            return True

    return False


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    total = 0

    for line in lines:
        split = line.split(":")
        res, nums = int(split[0]), list(map(int, split[1].split(" ")[1:]))
        print(nums) # print check to see if it's not stuck in an inf loop

        if generate_combinations(res, nums):
            total += res

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
