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

    sequences = {}

    for line in lines:
        secret_number = int(line)
        monkeys = [((secret_number % 10), None)]
        monkey_sequences = set()
        iterations = 2000

        for i in range(iterations):
            secret_number = predict_secret_number(secret_number)
            price = secret_number % 10
            monkeys.append((price, price - monkeys[i][0]))

            if i < 3:
                continue

            change_sequence = []

            for j in range(i - 2, i + 2):
                change_sequence.append(monkeys[j][1])

            change_sequence = tuple(change_sequence)

            if change_sequence not in monkey_sequences:
                monkey_sequences.add(change_sequence)

                if change_sequence not in sequences:
                    sequences[change_sequence] = price
                else:
                    sequences[change_sequence] += price

    total = max(sequences.values())

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
