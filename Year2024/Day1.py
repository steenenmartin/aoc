

with open("./Input/input1.txt") as f:
    input = f.readlines()

l1 = list(sorted([int(line.split()[0]) for line in input]))
l2 = list(sorted([int(line.split()[1]) for line in input]))


def part1():
    print(sum(abs(_l1 - _l2) for _l1, _l2 in zip(l1, l2)))


def part2():
    print(sum(_l1 * sum(_l1 == _l2 for _l2 in l2) for _l1 in l1))


if __name__ == "__main__":
    part1()
    part2()