from collections import Counter
from textwrap import dedent

import aoc

test_input = dedent("""\
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
""")


def part1(data):
    def iter_most_common_bits():
        for bits in zip(*data.strip().splitlines()):
            count = Counter(bits)
            [(mcb, _)] = count.most_common(1)
            yield mcb

    gamma = ""
    epsilon = ""

    for mcb in iter_most_common_bits():
        lcb = "1" if mcb == "0" else "0"
        gamma += mcb
        epsilon += lcb

    return int(gamma, 2) * int(epsilon, 2)


def test_part1():
    assert 198 == part1(test_input)


if __name__ == '__main__':
    data = aoc.read_input(__file__)
    print("Part 1", part1(data))
