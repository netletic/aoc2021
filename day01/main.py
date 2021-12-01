from __future__ import annotations

from more_itertools import windowed


def get_input(filename: str = "input.txt") -> int:
    with open("input.txt") as f:
        return [int(n) for n in f.readlines()]


def part1(numbers: list[int]) -> int:
    counter: int = 0
    for n1, n2 in zip(numbers, numbers[1:]):
        if n2 > n1:
            counter += 1
    return counter


def part2(numbers: list[int]) -> int:
    counter: int = 0
    window1, window2 = windowed(numbers, 3), windowed(numbers[1:], 3)
    for w1, w2 in zip(window1, window2):
        if sum(w2) > sum(w1):
            counter += 1
    return counter


def main() -> int:
    numbers = get_input()
    print(part1(numbers))
    print(part2(numbers))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
