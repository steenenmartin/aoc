import numpy as np
import math
import pipe

def part1():
    with open("Input/input10.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    last_open = []
    ss = 0
    for line in input:
        for s in line:
            if s in ("(", "[", "{", "<"):
                last_open.append(s)
            elif s == ")" and last_open[-1] != "(":
                ss += 3
                break
            elif s == "]" and last_open[-1] != "[":
                ss += 57
                break
            elif s == "}" and last_open[-1] != "{":
                ss += 1197
                break
            elif s == ">" and last_open[-1] != "<":
                ss += 25137
                break
            else:
                last_open.pop(-1)

    print(ss)


def part2():
    with open("Input/input10.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    ss = []
    for line in input:
        last_open = []
        corrupted = False
        for s in line:
            if s in ("(", "[", "{", "<"):
                last_open.append(s)
            elif s == ")" and last_open[-1] != "(":
                corrupted = True
                break
            elif s == "]" and last_open[-1] != "[":
                corrupted = True
                break
            elif s == "}" and last_open[-1] != "{":
                corrupted = True
                break
            elif s == ">" and last_open[-1] != "<":
                corrupted = True
                break
            else:
                last_open.pop(-1)

        local_sum = 0
        if not corrupted:
            for s in reversed(last_open):
                local_sum *= 5
                if s == "(":
                    local_sum += 1
                elif s == "[":
                    local_sum += 2
                elif s == "{":
                    local_sum += 3
                elif s == "<":
                    local_sum += 4

            ss.append(local_sum)
    ss_sorted = list(sorted(ss))
    print(ss_sorted[int((len(ss_sorted) - 1) / 2)])