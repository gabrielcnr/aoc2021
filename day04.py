from textwrap import dedent
from typing import List

import aoc

test_input = dedent("""\
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
""")


def bingo_parser(data, *, board_size=5):
    lines = (l.strip() for l in data.strip().splitlines())

    drawn_numbers = [int(i) for i in next(lines).split(",")]

    boards = []

    board = []

    for line in lines:
        if not line:
            continue
        row = [int(i) for i in line.split()]
        board.append(row)
        if len(board) == board_size:
            boards.append(board)
            board = []

    return drawn_numbers, boards


class Board:
    def __init__(self, size):
        self.num_to_cell = {}
        self.cell_state = {}
        self.size = size

    @classmethod
    def create(cls, board: List[List[int]]):
        b = cls(size=len(board))
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                b.num_to_cell[num] = (i, j)
                b.cell_state[(i, j)] = False
        return b

    def check_num(self, num: int) -> bool:
        if num in self.num_to_cell:
            cell = self.num_to_cell[num]
            self.cell_state[cell] = True
        return self.is_winner

    @property
    def is_winner(self):
        # check row-wise
        for i in range(self.size):
            if all(self.cell_state[i, j] for j in range(self.size)):
                return True

        # check column-wise
        for j in range(self.size):
            if all(self.cell_state[i, j] for i in range(self.size)):
                return True

        return False

    def get_sum_of_unmarked_numbers(self):
        return sum(n for n, cell in self.num_to_cell.items() if not self.cell_state[cell])


def part1(data):
    drawn_numbers, boards_data = bingo_parser(data)

    boards = [Board.create(board_data) for board_data in boards_data]

    for num in drawn_numbers:
        for board in boards:
            if board.check_num(num):
                # we have a winner
                unmarked_sum = board.get_sum_of_unmarked_numbers()
                return num * unmarked_sum

    raise


def test_bingo_parser():
    data = "1,2,3,4\n\n1 2\n3 4\n\n5 6\n7 8"

    drawn_numbers, boards = bingo_parser(data, board_size=2)

    assert [1, 2, 3, 4] == drawn_numbers

    assert [[[1, 2], [3, 4]],
            [[5, 6], [7, 8]]] == boards


def test_part1():
    assert 4512 == part1(test_input)


if __name__ == '__main__':
    data = aoc.read_input(__file__)
    print("Part 1", part1(data))
