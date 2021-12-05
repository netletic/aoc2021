from __future__ import annotations
from collections import Counter


with open("input.txt") as f:
    INPUT_S = f.read()


def transpose(input_s: str) -> list[str]:
    lines = input_s if isinstance(input_s, list) else input_s.strip().splitlines()
    bit_length = len(lines[0])

    result = []
    for _ in range(bit_length):
        result.append("")

    for row, line in enumerate(lines):
        for col, bit_string in enumerate(line):
            result[col] += bit_string

    return result


def count(input_l: list[str]):
    counter = {}
    for idx, bit_s in enumerate(input_l):
        counter[idx] = Counter(bit_s)
    return counter


def keep(counter, condition: str):
    keep = {}
    for idx, count in counter.items():
        if condition == "most_common":
            if count["0"] == count["1"]:
                keep[idx] = "1"
            else:
                keep[idx] = count.most_common()[0][0]
        elif condition == "least_common":
            if count["0"] == count["1"]:
                keep[idx] = "0"
            else:
                keep[idx] = count.most_common()[-1][0]
    return keep


def rating(condition: str):
    transposed = transpose(input_s=INPUT_S)
    ratings = INPUT_S.strip().splitlines()
    ratings_set = set(INPUT_S.strip().splitlines())

    counter = count(transposed)
    bits = keep(counter=counter, condition=condition)

    for i in range(len(ratings[0])):
        if len(ratings_set) == 1:
            break

        keeping_bit = bits[i]

        for rating in ratings:
            if rating[i] != keeping_bit:
                ratings_set.discard(rating)

        transposed = transpose(list(ratings_set))
        counter = count(transposed)
        bits = keep(counter=counter, condition=condition)

    return int(list(ratings_set)[0], 2)


def main() -> int:
    # part 1
    transposed = transpose(input_s=INPUT_S)
    counter = count(transposed)
    most_common_bits = keep(counter=counter, condition="most_common")
    least_common_bits = keep(counter=counter, condition="least_common")

    gamma_rate = int("".join(most_common_bits.values()), 2)
    epsilon_rate = int("".join(least_common_bits.values()), 2)
    print(gamma_rate * epsilon_rate)

    # part 2
    oxygen_rating = rating(condition="most_common")
    co2_rating = rating(condition="least_common")
    print(
        f"oxygen: {oxygen_rating}\tco2: {co2_rating}\tproduct: {oxygen_rating * co2_rating}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
