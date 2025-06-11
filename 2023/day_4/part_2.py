from queue import Queue

def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    total = 0
    cards = {}

    for i, line in enumerate(lines):
        line = line.split("|")
        winning = line[0]
        winning = winning.split(":")[1].strip(" ").split(" ")
        winning = [num for num in winning if num != ""]
        winning = set(map(int, winning))

        mine = line[1]
        mine = mine.strip(" ").split(" ")
        mine = [num for num in mine if num != ""]
        mine = map(int, mine)

        count = sum(1 for num in mine if num in winning)
        cards[i + 1] = count

    print(cards)

    queue = Queue()

    for key, val in cards.items():
        # Add to queue
        for i in range(val):
            queue.put(i + 1 + key)

    while not queue.empty():
        card = queue.get()
        total += 1
        matches = cards[card]
        for i in range(matches):
            queue.put(i + 1 + card)

    return total + len(cards.keys())


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
