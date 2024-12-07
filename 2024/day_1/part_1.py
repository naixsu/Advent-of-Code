def read_from_file(file_name: str) -> tuple[list, list]:
    left, right = [], []

    with open(file_name, "r") as file:
        for line in file:
            l = line.rstrip().split()
            left.append(int(l[0]))
            right.append(int(l[1]))

    left = sorted(left)
    right = sorted(right)
    
    return left, right


def get_total_distance() -> int:
    file_name = "day_1/input.txt"
    left, right = read_from_file(file_name)

    sum = 0

    for i, _ in enumerate(left):
        l = left[i]
        r = right[i]
        
        sum += abs(l-r)

    return sum


def main() -> None:
    sum = get_total_distance()
    print(sum)


if __name__ == "__main__":
    main()
