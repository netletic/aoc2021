from collections import defaultdict
from dataclasses import dataclass

INPUT_S = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


@dataclass(order=True, frozen=True)
class Coordinate:
    x: int
    y: int

    @classmethod
    def from_string(cls, input_s: str):
        x, y = input_s.split(",")
        return cls(x=int(x), y=int(y))


@dataclass
class Line:
    start: Coordinate
    end: Coordinate

    @property
    def horizontal(self):
        return self.start.y == self.end.y

    @property
    def vertical(self):
        return self.start.x == self.end.x

    @property
    def diagonal(self):
        return self.start.x != self.end.x and self.start.y != self.end.y

    @property
    def points(self):
        result = []

        if self.horizontal:
            y = self.start.y
            for x in range(self.start.x, self.end.x + 1):
                result.append(Coordinate(x, y))

        elif self.vertical:
            x = self.start.x
            for y in range(self.start.y, self.end.y + 1):
                result.append(Coordinate(x, y))

        elif self.diagonal:
            x_range = range(self.start.x, self.end.x + 1)
            y_increases = self.start.y < self.end.y

            if y_increases:
                y_range = range(self.start.y, self.end.y + 1)
            else:
                y_range = reversed(range(self.end.y, self.start.y + 1))

            for x, y in zip(x_range, y_range):
                result.append(Coordinate(x, y))

        else:
            raise AssertionError("shouldn't reach this")

        return result

    @classmethod
    def from_string(cls, input_s: str):
        co1_s, co2_s = input_s.split(" -> ")
        co1, co2 = Coordinate.from_string(co1_s), Coordinate.from_string(co2_s)
        return cls(start=co1, end=co2) if co1 < co2 else cls(start=co2, end=co1)


def read_input():
    with open("input.txt") as f:
        return f.read()


def main() -> int:
    dangerous = defaultdict(int)
    for inp in read_input().splitlines():
        line = Line.from_string(inp)
        for coordinate in line.points:
            dangerous[coordinate] += 1
    most_dangerous = [
        coordinate for coordinate, count in dangerous.items() if count >= 2
    ]
    print(len(most_dangerous))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
