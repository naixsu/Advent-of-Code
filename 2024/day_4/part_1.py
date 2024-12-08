def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    
    moves = [
        [(0, 0), (0, -1), (0, -2), (0, -3)],    # 0 Up
        [(0, 0), (0, 1), (0, 2), (0, 3)],       # 1 Down
        [(0, 0), (-1, 0), (-2, 0), (-3, 0)],    # 2 Left
        [(0, 0), (1, 0), (2, 0), (3, 0)],       # 3 Right
        [(0, 0), (1, -1), (2, -2), (3, -3)],    # 4 Top right
        [(0, 0), (-1, -1), (-2, -2), (-3, -3)], # 5 Top left
        [(0, 0), (-1, 1), (-2, 2), (-3, 3)],    # 6 Bottom left
        [(0, 0), (1, 1), (2, 2), (3, 3)],       # 7 Bottom right
    ]
    total = 0
    target = "XMAS"

    for row_index, line in enumerate(lines):
        for col_index, char in enumerate(line):

            if char != "X":
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
                    total += 1

    return total



def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
