def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sequences(lines: list[list[str]]) -> list[list[int]]:
    sequences = []

    for line in lines:
        sequences.append(
            list(map(int, line.split()))[::-1] # reverse the list
        )

    return sequences


def get_history(seq: list[int]) -> list[list[int]]:
    history = [[num for num in seq]]

    while any(history[-1]):
        next_history = []

        for i in range(1, len(history[-1])):
            # Get the difference
            next_history.append(
                history[-1][i] - history[-1][i-1]
            )

        history.append(next_history)

    return history


def extrapolate(history: list[list[int]]) -> int:
    for i in range(len(history) - 2, -1, -1): # reverse list
        history[i].append(
            history[i][-1] + history[i+1][-1]
        )

    return history[0][-1]


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    sequences = get_sequences(lines)

    total = 0

    for seq in sequences:
        history = get_history(seq)
        extrapolated = extrapolate(history)
        total += extrapolated

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
