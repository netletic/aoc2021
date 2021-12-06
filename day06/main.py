from __future__ import annotations
from collections import Counter

INPUT_S = "3,4,3,1,2"
with open("part1.txt") as f:
    INPUT_P1_S = f.read()


def parse_inputs(input_s: str) -> list[int]:
    ages = [int(n) for n in input_s.split(",")]
    return Counter(ages)


def n_fishes(days: int, ages: Counter):
    for day in range(days):
        n_zero_age = ages[0]
        for age in range(1, 9):
            n_age = ages[age]
            ages[age] -= n_age
            ages[age - 1] += n_age
        ages[6] += n_zero_age
        ages[8] += n_zero_age
        ages[0] -= n_zero_age
    return sum(ages.values())


def main() -> int:
    ages = parse_inputs(input_s=INPUT_P1_S)
    n_fish = n_fishes(days=256, ages=ages)
    print(n_fish)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
