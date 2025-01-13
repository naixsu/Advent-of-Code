def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def predict_secret_number(secret_number: int) -> int:
    def mix(num: int) -> int:
        return secret_number ^ num

    def prune() -> int:
        return secret_number % 16777216

    num = secret_number * 64
    secret_number = mix(num)
    secret_number = prune()

    num = secret_number // 32
    secret_number = mix(num)
    secret_number = prune()

    num = secret_number * 2048
    secret_number = mix(num)
    secret_number = prune()

    return secret_number


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    total = 0

    for line in lines:
        secret_number = int(line)

        for _ in range(2000):
            secret_number = predict_secret_number(secret_number)

        total += secret_number

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
