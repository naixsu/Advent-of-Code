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

    # If the tile is #, the new map contains ## instead.
    # If the tile is O, the new map contains [] instead.
    # If the tile is ., the new map contains .. instead.
    # If the tile is @, the new map contains @. instead.

    wide_maze = []

    for m in maze:
        w = ""
        for char in m:
            if char == "#":
                w += "##"
            elif char == "O":
                w += "[]"
            elif char == ".":
                w += ".."
            else:
                w += "@."

        wide_maze.append(w)
            
    return wide_maze, moves


def get_maze_hash(maze: list[list[str]]) -> dict:
    maze_hash = {}

    for j, line in enumerate(maze):
        for i, char in enumerate(line):

            if char not in maze_hash:
                maze_hash[char] = [(j, i)]
            else:
                maze_hash[char].append((j, i))
            

    return maze_hash


def get_connected_boxes(
    opens: list[tuple[int, int]], 
    closes: list[tuple[int, int]], 
    start: tuple[int, int],
    move: str,
) -> set:
    visited = set()
    queue = [start]

    move_dir = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    
    while queue:
        current = queue.pop(0)

        if current in visited:
            continue

        visited.add(current)
        
        if move in [">", "<"]:
            multiplier = 2
        else:
            multiplier = 1

        add = move_dir[move]
        next_from_open = current[0][0] + add[0] * multiplier, current[0][1] + add[1] * multiplier
        next_from_close = current[1][0] + add[0] * multiplier, current[1][1] + add[1] * multiplier

        if next_from_open not in opens and next_from_close not in closes and move in ["<", ">"]:
            continue

        if next_from_open in opens and next_from_close in closes:
            queue.append((next_from_open, next_from_close))

        if next_from_open in closes:
            if next_from_close in opens:
                left = next_from_open[0], next_from_open[1] - 1
                queue.append((left, next_from_open))
            else:
                left = next_from_open[0], next_from_open[1] - 1
                queue.append((left, next_from_open))

        if next_from_close in opens:
            if next_from_open in closes:
                right = next_from_close[0], next_from_close[1] + 1
                queue.append((next_from_close, right))
            else:
                right = next_from_close[0], next_from_close[1] + 1
                queue.append((next_from_close, right))

    return visited


def move_connected_boxes(
    connected_boxes: set,
    opens: list[tuple[int, int]], 
    closes: list[tuple[int, int]], 
    walls: list[tuple[int, int]],
    move: str,
) -> bool:

    move_dir = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }

    add = move_dir[move]
    for box in connected_boxes:

        for pos in box:
            next = pos[0] + add[0], pos[1] + add[1]

            if next in walls:
                return False

    for box in connected_boxes:
        left, right = box
        open_index = opens.index(left)
        close_index = closes.index(right)
        left = left[0] + add[0], left[1] + add[1]
        right = right[0] + add[0], right[1] + add[1]

        opens[open_index] = left
        closes[close_index] = right

    return True


def move_sub(maze: list[list[str]], maze_hash: dict, moves: list[str]) -> int:
    # Invert X Y
    move_dir = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }

    sub = maze_hash["@"][0]
    walls = maze_hash["#"]
    opens = maze_hash["["]
    closes = maze_hash["]"]

    for move in moves:
        add = move_dir[move]
        next = sub[0] + add[0], sub[1] + add[1]

        if next in walls:
            continue

        if move in [">", "<"]:
            if next not in opens and next not in closes:
                sub = next
                continue

            if next in opens:
                index = opens.index(next)
            else:
                index = closes.index(next)

            op, cl = opens[index], closes[index]

            connected_boxes = get_connected_boxes(
                opens, closes, (op, cl), move,
            )

            if move_connected_boxes(
                connected_boxes, opens, closes,
                walls, move,
            ):
                sub = next
            else:
                sub = sub

        if move in ["^", "v"]:
            if next not in opens and next not in closes:
                sub = next
                continue
            
            if next in opens:
                index = opens.index(next)
            else:
                index = closes.index(next)
            
            op, cl = opens[index], closes[index]

            connected_boxes = get_connected_boxes(
                opens, closes, (op, cl), move,
            )

            if move_connected_boxes(
                connected_boxes, opens, closes,
                walls, move,
            ): 
                sub = next
            else:
                sub = sub


    total = 0

    for open in opens:
        total += 100 * open[0] + open[1]

    return total

def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")
    maze, moves = init(lines)
    maze_hash = get_maze_hash(maze)

    total = move_sub(maze, maze_hash, moves)


    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
