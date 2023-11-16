import itertools
from collections import Counter

import memoize as memoize
import numpy as np


def part1():
    with open("Input/input14.txt") as fp:
        count = 0
        pair_insertions = {}
        while True:
            line = fp.readline().strip("\n")
            if not line and count > 1:
                break

            if count == 0:
                polymer_template = line
            elif count == 1:
                pass
            else:
                pair_insetion = line.split("->")
                pair_insertions[pair_insetion[0].strip(" ")] = pair_insetion[1].strip(" ")

            count += 1


        for i in range(10):
            print(i)
            result_string = ""
            for i in range(len(polymer_template)):
                sub = polymer_template[i:i+2]

                if sub in pair_insertions:
                    result_string += sub[0] + pair_insertions[sub]
            result_string += polymer_template[-1]
            polymer_template = result_string

        counts = {x: result_string.count(x) for x in result_string}
        max_count = max(counts.values())
        min_count = min(counts.values())

        print(max_count-min_count)


pair_insertions = dict()


def part2():
    with open("Input/input14.txt") as fp:
        count = 0
        while True:
            line = fp.readline().strip("\n")
            if not line and count > 1:
                break

            if count == 0:
                polymer_template = line
            elif count == 1:
                pass
            else:
                pair_insetion = line.split("->")
                pair_insertions[pair_insetion[0].strip(" ")] = pair_insetion[1].strip(" ")

            count += 1

    count_dict = dict()
    for i in range(len(polymer_template)-1):
        substring = polymer_template[i:i + 2]
        count_dict = dict(Counter(count_dict) + Counter(freq_map(0, substring[0], substring[1])))
    count_dict[polymer_template[-1]] += 1

    print(max(count_dict.values()) - min(count_dict.values()))

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def freq_map(depth, left, right):
    if depth == 40:
        return {left: 1}
    else:
        return dict(
            Counter(freq_map(depth + 1, left, pair_insertions["".join([left, right])]))
            + Counter(freq_map(depth + 1, pair_insertions["".join([left, right])], right))
        )


