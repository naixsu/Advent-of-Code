def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def init(lines: list[list[str]]) -> tuple[list[list[str]], list[str]]:
    maze, moves = [], []
    in_maze = True

    for line in lines:
        if line == "":
            in_maze = False
            continue

        if in_maze:
            maze.append(line)
        else:
            moves.append(line)

    moves = [j for i in moves for j in i]
    
    return maze, moves


def get_maze_hash(maze: list[list[str]]) -> dict:
    maze_hash = {}

    for j, line in enumerate(maze):
        for i, char in enumerate(line):
            if char not in maze_hash:
                maze_hash[char] = [(j, i)]
            else:
                maze_hash[char].append((j, i))

    return maze_hash


def move_sub(maze_hash: dict, moves: list[str]) -> int:
    # Invert X Y
    move_dir = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }

    sub = maze_hash["@"][0]
    walls = maze_hash["#"]
    boxes = maze_hash["O"]

    for move in moves:
        queue = []
        add = move_dir[move]
        next = sub[0] + add[0], sub[1] + add[1]

        if next in walls:
            continue

        if next in boxes:
            queue = [next]

            while queue:
                next_box = queue[-1][0] + add[0], queue[-1][1] + add[1]

                if next_box in boxes:
                    queue.append(next_box)
                    continue

                current_box = queue.pop()
                box_index = boxes.index(current_box)
                moved_box = current_box[0] + add[0], current_box[1] + add[1]

                if moved_box not in walls:
                    boxes[box_index] = moved_box
                else:
                    sub = sub
                    break
                sub = next
            continue

        sub = next


    total = 0

    for box in boxes:
        total += 100 * box[0] + box[1]
    
    return total


def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    maze, moves = init(lines)
    maze_hash = get_maze_hash(maze)
    total = move_sub(maze_hash, moves)

    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
