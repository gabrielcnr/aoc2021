import aoc


def part1(data: str, *, days_after: int = 0):
    fishes = [int(n) for n in data.strip().split(",")]

    while days_after:
        fishes_now = fishes[:]
        for i, fish in enumerate(fishes_now):
            fish -= 1
            if fish == -1:
                fishes.append(8)
                fishes[i] = 6
            else:
                fishes[i] = fish
        # print(fishes)

        days_after -= 1

    return len(fishes)


test_input = "3,4,3,1,2"


def test_part1():
    assert 26 == part1(test_input, days_after=18)
    assert 5934 == part1(test_input, days_after=80)


if __name__ == '__main__':
    data = aoc.read_input(__file__)
    print("Part1", part1(data, days_after=80))