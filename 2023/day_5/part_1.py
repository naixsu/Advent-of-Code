def read_from_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        line = file.read()

    return line


def get_map(line: list[int], lst: list[tuple[int, int, int]]) -> None:
    dst, src, rng = line
    lst.append((src, dst, rng))


def lookup(val: int, mappings: list[tuple[int, int, int]]) -> int:
    for src, dst, rng in mappings:
        if src <= val < src + rng:
            return dst + (val - src)
    return val


def init(lines: list[str]) -> tuple[list[int], dict, dict, dict, dict, dict, dict, dict]:
    seeds = []
    maps = [[] for _ in range(7)]
    state = -1
    map_labels = [
        "seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:",
        "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:",
        "humidity-to-location map:",
    ]

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if "seeds" in line:
            seeds = list(map(int, line.split(":")[1].strip().split()))
            continue

        for i, label in enumerate(map_labels):
            if line == label:
                state = i
                break
        else:
            get_map(list(map(int, line.split())), maps[state])

    return (seeds, *maps)



def get_sum() -> int:
    file_name = "input.txt"
    lines = read_from_file(file_name).split("\n")

    seeds, sts, stf, ftw, wtl, ltt, tth, htl = init(lines)

    total = float("inf")

    for seed in seeds:
        soil = lookup(seed, sts)
        fert = lookup(soil, stf)
        water = lookup(fert, ftw)
        light = lookup(water, wtl)
        temp = lookup(light, ltt)
        humid = lookup(temp, tth)
        location = lookup(humid, htl)

        total = min(total, location)


    return total


def main() -> None:
    sum = get_sum()
    print(sum)


if __name__ == "__main__":
    main()
