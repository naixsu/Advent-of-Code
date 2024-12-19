def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def arrange_block(block: list[str]) -> list[str]:
    block = list(block)
    left, right = 0, len(block) - 1

    while left < right:
        print(left, right)
        if block[left] != ".":
            left += 1
        elif block[left] == ".":
            block[left], block[right] = block[right], block[left]
            right -= 1

    return block


def check_sum(block: list[str]) -> int:
    total = 0

    for index, val in enumerate(block):
        if val == ".":
            return total
        total += int(index) * int(val)

    return total


def get_pairs(lines: str) -> list[tuple[int, int]]:
    pairs = []

    for i in range(0, len(lines), 2):
        pairs.append((lines[i], lines[i+1]))

    return pairs


def get_block(pairs: list[tuple[int, int]]) -> list[str]:
    block = []

    for file_id, pair in enumerate(pairs):
        for _ in range(int(pair[0])):
            block.append(str(file_id))

        for _ in range(int(pair[1])):
            block.append(".")

    return block


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")[0] # In case it has "\n"

    # Put no op at the end of the line
    if len(lines) % 2 == 1:
        lines += "0"

    pairs = get_pairs(lines)
    block = get_block(pairs)
    block = arrange_block(block)
    total = check_sum(block)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
