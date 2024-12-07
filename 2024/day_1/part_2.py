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


def build_hash(left: list[int], right: list[int]) -> dict:
    sim_hash = {}

    for num in right:
        if num not in sim_hash:
            sim_hash[num] = 0
        if num in left:
            sim_hash[num] += 1

    return sim_hash


def get_similarity_score() -> int:
    file_name = "input.txt"
    left, right = read_from_file(file_name)
    sim_hash = build_hash(left, right)
    
    sum = 0

    for key, val in sim_hash.items():
        sum += key * val

    return sum


def main() -> None:
    sum = get_similarity_score()
    print(sum)


if __name__ == "__main__":
    main()
