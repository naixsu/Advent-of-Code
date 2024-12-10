def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def setup(lines: list[str]) -> tuple[dict, list[str]]:
    ordering_rules = []
    page_orders = []
    before_empty_found = False

    for item in lines:
        if item == '':
            before_empty_found = True
        if before_empty_found:
            page_orders.append(item)
        else:
            ordering_rules.append(item)

    page_orders = page_orders[1:-1] # Assuming last character is new line

    rules = {}

    for order in ordering_rules:
        split = order.split("|")
        left, right = split[0], split[1]

        if left not in rules:
            rules[left] = [order]
        else:
            rules[left].append(order)

        if right not in rules:
            rules[right] = [order]
        else:
            rules[right].append(order)

    return rules, page_orders


def is_safe_order(page_order: list[str], rules: dict) -> bool:
    found = set()
    found.add(page_order[0])
    for num in page_order[1:]:
        rule = rules.get(num, [])
        for r in rule:
            left, right = r.split("|")
            if left == right:
                return False
            if num == left and (num in found or right in found):
                return False
        found.add(num)
    return True


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    rules, page_orders = setup(lines)

    total = 0

    for page_order in page_orders:
        page_order = page_order.split(",")
        if is_safe_order(page_order, rules):
            middle_index = len(page_order) // 2
            total += int(page_order[middle_index])

    return total



def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()