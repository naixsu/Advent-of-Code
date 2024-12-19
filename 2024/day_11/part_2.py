def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).strip().split(" ")

    # If stone is 0, replace with 1
    # If stone is even, split - no leading zeroes
    # Else, multiply by 2024
    stones = [line for line in lines]
    blinks = 75
    stone_map = {}
    for stone in stones:
        if stone not in stone_map:
            stone_map[stone] = 1
        else:
            stone_map[stone] += 1

    for _ in range(blinks):
        new = {}

        for key, value in stone_map.items():
            if key == "0":
                transform = "1"
                if transform not in new:
                    new[transform] = value
                else:
                    new[transform] += value
            else:
                mid, odd = divmod(len(key), 2)
                if odd:
                    transform = int(key) * 2024
                    transform = str(transform)
                    if transform not in new:
                        new[transform] = value
                    else:
                        new[transform] += value
                else:
                    first, second = str(int(key[:mid])), str(int(key[mid:]))
                    if first not in new:
                        new[first] = value
                    else:
                        new[first] += value
                    if second not in new:
                        new[second] = value
                    else:
                        new[second] += value

        stone_map = new

    total = 0

    for value in stone_map.values():
        total += value

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()