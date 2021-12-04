from collections import defaultdict


EXAMPLE_BOARD = """
14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

INPUT_S = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


class Board:
    def __init__(self, board_s: str):
        self.board = []
        self.numbers = set()
        # rows
        for row in board_s.strip().splitlines():
            self.board.append({int(n) for n in row.split()})
            for n in row.split():
                self.numbers.add(int(n))

        # columns
        self.board_transpose = []
        for i in range(5):
            self.board_transpose.append(["", "", "", "", ""])
        for i, row in enumerate(board_s.strip().splitlines()):
            for j, number in enumerate(row.split()):
                self.board_transpose[j][i] = int(number)
        self.board_columns = []
        for row in self.board_transpose:
            self.board_columns.append(set(row))
        self.numbers_hit = set()
        self.numbers_hit_in_row = defaultdict(int)
        self.numbers_hit_in_column = defaultdict(int)
        self.board_has_won = False

    def __str__(self):
        return str(self.board)

    @property
    def numbers_unhit(self):
        return self.numbers - self.numbers_hit

    def number_drawn(self, number: int):
        """We wil take in the newly drawn number.
            1. we will update numbers_hit
            2. we will keep state of n_hits in every row
            2.a win condition sets in when n_hits for that row equals 5

        Args:
            number (int): [description]
        """
        if not self.board_has_won:
            if number in self.numbers:
                self.numbers_hit.add(number)

            for idx, row in enumerate(self.board):
                if number in row:
                    self.numbers_hit_in_row[idx] += 1
                    if self.numbers_hit_in_row[idx] == 5:
                        score = sum(self.numbers_unhit) * number
                        self.board_has_won = True
                        return score

            for idx, row in enumerate(self.board_columns):
                if number in row:
                    self.numbers_hit_in_column[idx] += 1
                    if self.numbers_hit_in_column[idx] == 5:
                        score = sum(self.numbers_unhit) * number
                        self.board_has_won = True
                        return score


def create_boards(input_s: str = INPUT_S):
    boards = []
    for block in input_s.split("\n\n"):
        if "," in block:
            continue
        boards.append(Board(block))
    return boards


def create_draws(input_s: str = INPUT_S):
    numbers = []
    for line in input_s.splitlines()[:2]:
        for n in line.split(","):
            if n:
                numbers.append(int(n))
    return numbers


def main() -> int:
    with open("input.txt") as f:
        input_s = f.read()
    # boards = create_boards()
    # numbers = create_draws()
    boards = create_boards(input_s)
    numbers = create_draws(input_s)
    for number in numbers:
        for board in boards:
            score = board.number_drawn(number)
            if score:
                print(score)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
