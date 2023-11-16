import numpy as np

def part1():
    with open("./Year2015/Input/input5.txt") as fp:
        inputs = [x.strip("\n") for x in fp.readlines()]

    nice_strings = 0

    vowels = ('a', 'e', 'i', 'o', 'u')
    banned_strings = ('ab', 'cd', 'pq', 'xy')

    for input in inputs:
        if any(x in input for x in banned_strings):
            continue

        double_count = sum(input[idx] == j for idx, j in enumerate(input, 1) if idx != len(input))
        vowel_count = sum(1 for char in input if char in vowels)

        if double_count and vowel_count >= 3:
            nice_strings += 1

    print(nice_strings)


def part2():
    with open("./Year2015/Input/input5.txt") as fp:
        inputs = [x.strip("\n") for x in fp.readlines()]

    nice_strings = 0

    for input in inputs:
        repeating_pair = False
        divided_repeat = False

        pairs = set()
        prev_pair = ""
        for i, s in enumerate(input):
            if i >= 1 and not repeating_pair:
                pair = input[i - 1:i+1]

                if pair in pairs and not prev_pair == pair:
                    repeating_pair = True

                prev_pair = pair

                pairs.add(pair)


            if i >= 2 and not divided_repeat:
                s1 = input[i-2:i-1]
                if s1 == s:
                    divided_repeat = True

        if repeating_pair and divided_repeat:
            nice_strings += 1

    print(nice_strings)