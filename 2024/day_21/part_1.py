def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read()


def get_pads() -> tuple[dict, dict]:
    # Keeping the inverted (Y, X) for consistency with the other
    # problems :D

    numpad = {
        "7": (0, 0), "8": (0, 1), "9": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "1": (2, 0), "2": (2, 1), "3": (2, 2),
        "0": (3, 1), "A": (3, 2),
    }
    dirpad = {
        "^": (0, 1), "A": (0, 2),
        "<": (1, 0), "v": (1, 1),
        ">": (1, 2),
    }

    return numpad, dirpad


def precompute_all_shortest_paths(pad: dict) -> dict:
    moves = {(-1, 0): "^", (0, 1): ">", (1, 0): "v", (0, -1): "<"}

    def bfs(start: tuple[int, int]) -> dict:
        queue = [(start, 0, "")]
        visited = set()
        paths = {}

        while queue:
            curr, steps, seq = queue.pop(0)

            # If a shorter path already exists, skip this node
            if curr in visited and steps > paths[curr][0]:
                continue

            if curr not in paths:
                paths[curr] = (steps, [seq + "A"])
            else:
                # If another path of the same length is found, add it
                if steps == paths[curr][0]:
                    paths[curr][1].append(seq + "A")

            visited.add(curr)

            y, x = curr
            for move, dir in moves.items():
                dy, dx = move
                next_pos = (y + dy, x + dx)

                if next_pos in pad.values() and next_pos not in visited:
                    queue.append((next_pos, steps + 1, seq + dir))

        return {
            k: v[1] for k, v in paths.items()
        }

    return {
        pos: bfs(pos) for pos in pad.values()
    }


def get_sequence_combinations(sequences: list[list[str]]) -> list[list[str]]:
    def backtrack(index, path):
        if index == len(sequences):
            combinations.append(''.join(path))
            return

        for choice in sequences[index]:
            path.append(choice)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])

    return combinations


def get_sequences(code: str, numpad: dict, precomputed_paths: dict):
    curr = numpad["A"]
    seqs = []

    for char in code:
        target = numpad[char]
        seqs.append(precomputed_paths[curr][target])
        curr = target

    sequences = get_sequence_combinations(seqs)

    return sequences


def get_numeric_code(code: str) -> int:
    return int(code[:-1])


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    numpad, dirpad = get_pads()
    numpad_precomputed_paths = precompute_all_shortest_paths(numpad)
    dirpad_precomputed_paths = precompute_all_shortest_paths(dirpad)
    total = 0

    for p1_code in lines:
        print("CODE", p1_code)
        numeric_code = get_numeric_code(p1_code)
        p1_sequences = get_sequences(p1_code, numpad, numpad_precomputed_paths)
        min_length = float("inf")

        for p1_seq in p1_sequences:
            p2_sequences = get_sequences(p1_seq, dirpad, dirpad_precomputed_paths)

            for p2_seq in p2_sequences:
                p3_sequences = get_sequences(p2_seq, dirpad, dirpad_precomputed_paths)

                for p3_seq in p3_sequences:
                    min_length = min(len(p3_seq), min_length)

        total += numeric_code * min_length

    return total

def main() -> None:
    total = get_sum()
    print(total)

if __name__ == "__main__":
    main()
