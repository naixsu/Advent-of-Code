def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "test.txt"
    lines = read_from_file(file_name).split("\n")
    """ Cases
    S.S  M.M  S.M   M.S
    .A.  .A.  .A.   .A.
    M.M  S.S  S.M   M.S
    """
    moves = [
        # A in the middle; look for MAS
        [(-1, -1), (0, 0), (1, 1)], # Top left to bottom right
        [(1, -1), (0, 0), (-1, 1)], # Top right to bottom left
        [(-1, 1), (0, 0), (1, -1)], # Bottom left to top right
        [(1, 1), (0, 0), (-1, -1)], # Bottom right to top left
    ]
    total = 0
    target = "MAS"
    mas = {}

    for row_index, line in enumerate(lines):
        for col_index, char in enumerate(line):
            #
            if char != "A":
                continue

            for move in moves:
                word = ""
                for dy, dx in move:
                    new_row = row_index + dy
                    new_col = col_index + dx
                    # Ensure indices are within bounds
                    if 0 <= new_row < len(lines) and 0 <= new_col < len(lines[new_row]):
                        word += lines[new_row][new_col]
                    else:
                        break

                if word == target:
                    key = (row_index, col_index)
                    if key not in mas:
                        mas[key] = 0
                    else:
                        mas[key] += 1

    total = sum(value for value in mas.values() if value == 1)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
