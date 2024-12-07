def read_from_file(file_name: str) -> list:
    levels = []
    with open(file_name, "r") as file:
        for line in file:
            level = [int(x) for x in line.rstrip().split()]
            levels.append(level)
    
    return levels


def is_safe(level: list[int]) -> bool:
    # Determine order:
    decreasing = level[0] > level[1]
    safe = True

    for i, j in zip(level, level[1:]):
        diff = abs(i-j)
        oob = not (1 <= diff <= 3) # out of bounds
        ooo = (decreasing and i < j) or (not decreasing and i > j) # out of order

        if oob or ooo:
            safe = False
            break

    return safe

def is_tolerable_report(level: list[int]) -> bool:
    for index in range(len(level)):
        new_level = level[:index] + level[index+1:]

        if is_safe(new_level):
            return True

    return False


def get_safe_reports() -> int:
    file_name = "day_2/input.txt"
    levels = read_from_file(file_name)
    sum = 0

    for level in levels:
        safe = is_tolerable_report(level)

        if safe:
            sum += 1

    return sum


def main() -> None:
    sum = get_safe_reports()
    print(sum)


if __name__ == "__main__":
    main()
