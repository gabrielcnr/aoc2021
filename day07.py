import statistics

import aoc

test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def part1(data):
    median = statistics.median(data)
    costs = sum(abs(x - median) for x in data)
    return costs


def test_part1():
    assert 37 == part1(test_input)


if __name__ == '__main__':
    data = aoc.read_input(__file__)
    data = [int(n) for n in data.strip().split(",")]
    print("Part 1", part1(data))
