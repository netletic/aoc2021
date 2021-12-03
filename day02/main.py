from collections import Counter


def get_vectors_from_input(filename: str):
    vectors = Counter()
    with open(filename) as f:
        for line in f.readlines():
            direction, magnitude = line.split()
            vectors[direction] += int(magnitude)
    vectors["depth"] = vectors["down"] - vectors["up"]
    return vectors


def get_vectors_from_input2(filename: str):
    vectors = Counter()
    with open(filename) as f:
        for line in f.readlines():
            direction, magnitude = line.split()
            magnitude = int(magnitude)
            if direction == "up":
                vectors["aim"] -= magnitude
            if direction == "down":
                vectors["aim"] += magnitude
            if direction == "forward":
                vectors[direction] += magnitude
                vectors["depth"] += vectors["aim"] * magnitude
    return vectors


def part1():
    vectors = get_vectors_from_input("input.txt")
    print(vectors)
    result = vectors["depth"] * vectors["forward"]
    print(result)


def part2():
    vectors = get_vectors_from_input2("input.txt")
    print(vectors)
    result = vectors["depth"] * vectors["forward"]
    print(result)


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
