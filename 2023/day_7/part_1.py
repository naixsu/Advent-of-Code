def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_hand_bid(lines: list[str]) -> dict:
    hand_bid = {}

    for line in lines:
        hand, bid = line.split()
        hand_bid[hand] = int(bid)

    return hand_bid


def determine_card_type(hand: str) -> str:
    """
    Five of a kind: [5]
    Four of a kind: [4, 1] or [1, 4]
    Full house: [3, 2] or [2, 3]
    Three of a kind: [3, 1, 1] or [1, 3, 1] or [1, 1, 3]
    Two pair: [2, 2, 1] or [2, 1, 2] or [1, 2, 2]
    One pair: [2, 1, 1, 1] or [1, 2, 1, 1] or [1, 1, 2, 1] or [1, 1, 1, 2]
    High card: [1, 1, 1, 1, 1]
    """

    types = {
        "[5]": "Five",
        "[1, 4]": "Four",
        "[2, 3]": "Full",
        "[1, 1, 3]": "Three",
        "[1, 2, 2]": "Two",
        "[1, 1, 1, 2]": "One",
        "[1, 1, 1, 1, 1]": "High",

    }

    counter = {}

    for char in hand:
        counter[char] = counter.get(char, 0) + 1

    freq = sorted(list(counter.values()))

    return types[str(freq)]


def get_pairs(hand_bid: dict) -> dict:
    pairs = {}

    hands = hand_bid.keys()

    for hand in hands:
        card_type = determine_card_type(hand)
        pairs.setdefault(card_type, []).append(hand)

    return pairs


def determine_card_ranks(hands: list[str]) -> list[str]:
    if len(hands) == 1:
        return hands

    """
    Order:
    A -> K -> Q -> J -> T -> 9 -> 8 -> 7 -> 6
    -> 5 -> 4 -> 3 -> 2
    """
    order = {
        "A" : 14, "K": 13, "Q": 12, "J": 11,
        "T": 10, "9": 9, "8": 8, "7": 7, "6": 6,
        "5": 5, "4": 4, "3": 3, "2": 2,
    }

    def card_strengths(hand: str):
        return [order[c] for c in hand]

    return sorted(hands, key=card_strengths)


def get_winnings(hand_bid: dict, pairs: dict):
    winnings = 0
    """
    Strongest to weakest:
    Five -> Four -> Full -> Three -> Two -> One -> High
    """
    card_types = [
        "High", "One", "Two", "Three",
        "Full", "Four", "Five",
    ]
    rank = 1

    for card_type in card_types:
        try:
            hands = pairs.pop(card_type)
            hands = determine_card_ranks(hands)

            for hand in hands:
                winnings += hand_bid[hand] * rank
                rank += 1
        except:
            continue


    return winnings


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    hand_bid = get_hand_bid(lines)
    pairs = get_pairs(hand_bid)

    total = get_winnings(hand_bid, pairs)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
