import math
from itertools import combinations


def part1():
    with open("./Year2015/Input/input17.txt") as fp:
        input = [int(x) for x in fp.readlines()]

    sum_150_combs = 0
    for r in range(len(input)):
        combs = combinations(input, r)
        for c in combs:
            if sum(c) == 150:
                sum_150_combs += 1

    print(sum_150_combs)


def part2():
    with open("./Year2015/Input/input17.txt") as fp:
        input = [int(x) for x in fp.readlines()]

    min_count = math.inf
    for r in range(len(input)):
        combs = combinations(input, r)
        for c in combs:
            if sum(c) == 150:
                container_count = len(c)

                if container_count < min_count:
                    min_count = container_count

    min_combs = combinations(input, min_count)
    sum_150_min_comb_count = 0
    for c in min_combs:
        if sum(c) == 150:
            sum_150_min_comb_count += 1

    print(sum_150_min_comb_count)



