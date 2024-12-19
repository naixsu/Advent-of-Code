def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def arrange_block(block: list[list[str]]) -> list[str]:
    block = list(block)
    left, right = 0, len(block) - 1

    while right != 0:
        if "." in block[right]:
            right -= 1
            continue

        len_right = len(block[right])

        for l in range(right):
            len_left = block[l].count(".")
            if len_left == 0:
                continue
            if len_left >= len_right:
                r = 0
                for i in range(len(block[l])):
                    if r > len(block[right]) - 1:
                        break
                    if block[l][i] == ".":
                        block[l][i], block[right][r] = block[right][r], block[l][i]
                        r += 1
        right -= 1

    block = [
        x
        for xs in block
        for x in xs
    ]

    return block


def check_sum(block: list[str]) -> int:
    total = 0

    for index, val in enumerate(block):
        if val == ".":
            continue
        total += int(index) * int(val)

    return total


def get_pairs(lines: str) -> list[tuple[int, int]]:
    pairs = []

    for i in range(0, len(lines), 2):
        pairs.append((lines[i], lines[i+1]))

    return pairs


def get_block(pairs: list[tuple[int, int]]) -> list[list[str]]:
    block = []

    for file_id, pair in enumerate(pairs):
        file_block, dot_block = [], []

        for _ in range(int(pair[0])):
            file_block.append(str(file_id))

        if file_block:
            block.append(file_block)

        for _ in range(int(pair[1])):
            dot_block.append(".")

        if dot_block:
            block.append(dot_block)

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
