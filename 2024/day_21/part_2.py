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


def initialize_pads() -> None:
    global numpad, dirpad, numpad_precomputed_paths, dirpad_precomputed_paths
    numpad, dirpad = get_pads()
    numpad_precomputed_paths = precompute_all_shortest_paths(numpad)
    dirpad_precomputed_paths = precompute_all_shortest_paths(dirpad)


def remove_zigzags(paths: dict) -> dict:
    cleaned_paths = {}

    def is_zigzag(seq: str) -> bool:
        if seq == "A" or len(seq) < 4:
            return False

        # These are seqs that are length >= 4
        # Ex: >v>A
        for i in range(2, len(seq)):
            if (
                seq[i - 2] == seq[i] and
                seq[i - 1] != seq[i]
            ):
                return True

        return False

    for key, val in paths.items():
        cleaned_paths[key] = {}

        for k, v in val.items():
            non_zigzags = [seq for seq in v if not is_zigzag(seq)]
            cleaned_paths[key][k] = non_zigzags


    return cleaned_paths


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
            # If another path of the same length is found, add it
            elif steps == paths[curr][0]:
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

    paths = { pos: bfs(pos) for pos in pad.values() }
    paths = remove_zigzags(paths)

    return paths


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


def get_sequences(code: str, pad: dict, precomputed_paths: dict) -> list[list[str]]:
    curr = pad["A"]
    seqs = []

    for char in code:
        target = pad[char]
        seqs.append(precomputed_paths[curr][target])
        curr = target

    sequences = get_sequence_combinations(seqs)

    return sequences


def get_numeric_code(code: str) -> int:
    return int(code[:-1])


def get_shortest_seq(keys, depth, cache):
    if depth == 0:
        return len(keys)

    if (keys, depth) in cache:
        return cache[(keys, depth)]

    total = 0

    for start, target in zip("A" + keys, keys):
        s, t = dirpad[start], dirpad[target]
        sequences = dirpad_precomputed_paths[s][t]
        total += min(
            get_shortest_seq(seq, depth - 1, cache)
            for seq in sequences
        )

    cache[(keys, depth)] = total
    return total


# Global variables
numpad, dirpad = None, None
numpad_precomputed_paths, dirpad_precomputed_paths = None, None


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    initialize_pads()
    total = 0
    max_depth = 25
    cache = {}

    for p1_code in lines:
        numeric_code = get_numeric_code(p1_code)
        p1_sequences = get_sequences(p1_code, numpad, numpad_precomputed_paths)
        min_length = float("inf")

        for p1_seq in p1_sequences:
            min_length = min(
                min_length,
                get_shortest_seq(p1_seq, max_depth, cache)
            )

        total += numeric_code * min_length

    return total

def main() -> None:
    sum = get_sum()
    print(sum)

if __name__ == "__main__":
    main()
