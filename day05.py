from collections import Counter
from dataclasses import dataclass
from functools import cached_property
from textwrap import dedent

import aoc

test_input = dedent("""\
    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2\
""")


def parse(data):
    @dataclass(frozen=True)
    class Point:
        x: int
        y: int

    class Line:
        def __init__(self, origin: Point, dest: Point):
            self.origin = origin
            self.dest = dest

            self.x_step = self.get_step(origin.x, dest.x)
            self.y_step = self.get_step(origin.y, dest.y)

        @staticmethod
        def get_step(v1, v2):
            if v1 < v2:
                return 1
            elif v1 > v2:
                return -1
            else:
                return 0

        @cached_property
        def points(self):
            def iter_points():
                p = self.origin
                while p != self.dest:
                    yield p
                    p = Point(x=p.x + self.x_step,
                              y=p.y + self.y_step)
                yield self.dest

            return list(iter_points())

    lines = []
    for input_line in data.strip().splitlines():
        input_line = input_line.strip()
        left, right = input_line.split(" -> ")
        x1, y1 = [int(n) for n in left.split(",")]
        x2, y2 = [int(n) for n in right.split(",")]
        origin = Point(x1, y1)
        dest = Point(x2, y2)
        line = Line(origin, dest)
        lines.append(line)

    return lines


def part1(data):
    lines = parse(data)

    covered_points = Counter()

    for line in lines:
        if line.origin.x != line.dest.x and line.origin.y != line.dest.y:
            continue

        for point in line.points:
            covered_points[point] += 1

    return sum(1 for x in covered_points.values() if x > 1)


def part2(data):
    lines = parse(data)

    covered_points = Counter()

    for line in lines:
        for point in line.points:
            covered_points[point] += 1

    return sum(1 for x in covered_points.values() if x > 1)


def test_part1():
    assert 5 == part1(test_input)


def test_part2():
    assert 12 == part2(test_input)

if __name__ == '__main__':
    data = aoc.read_input(__file__)
    print("Part 1", part1(data))
    print("Part 2", part2(data))
