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
    dupes = {}

    # Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
    # Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
    # Your copy of card 2 also wins one copy each of cards 3 and 4.
    # Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
    # Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
    # Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
    # Your one instance of card 6 (one original) has no matching numbers and wins no more cards.

    # This needs more work

    for key, val in cards.items():
        for i in range(val):
            print(i, key, i + key)
            dupes[i + key + 1] = dupes.get(i + key + 1, 0) + 1


    print(dupes)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
