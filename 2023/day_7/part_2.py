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
    freq_map = {}
    jokers = 0

    for card in hand:
        if card == "J":
            jokers += 1
        else:
            freq_map[card] = freq_map.get(card, 0) + 1

    if not freq_map:
        return "Five"  # All Jokers

    freqs = sorted(freq_map.values(), reverse=True)
    freqs[0] += jokers
    freqs = sorted(freqs)

    if freqs == [5]:
        return "Five"
    elif freqs == [1, 4]:
        return "Four"
    elif freqs == [2, 3]:
        return "Full"
    elif freqs == [1, 1, 3]:
        return "Three"
    elif freqs == [1, 2, 2]:
        return "Two"
    elif freqs == [1, 1, 1, 2]:
        return "One"
    elif freqs == [1, 1, 1, 1, 1]:
        return "High"
    else:
        return "Unknown"


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
        "5": 5, "4": 4, "3": 3, "2": 2, "J": 1
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
