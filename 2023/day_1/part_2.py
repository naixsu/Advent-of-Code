def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    char_map = {
        "o": [2], "t": [2, 4], "f": [3],
        "s": [2, 4], "e": [4], "n": [3],
    }

    num_map = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9",
    }

    total = 0

    for line in lines:
        nums = []

        for i, char in enumerate(line):

            if char in char_map:
                for vals in char_map[char]:
                    num = line[i : i + vals + 1]

                    if num in num_map:
                        nums.append(num_map[num])
                        continue

            elif char.isdigit():
                nums.append(char)

        if len(nums) == 1:
            total += int(nums[0] + nums[0])
        else:
            total += int(nums[0] + nums[-1])

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
