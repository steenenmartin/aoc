import numpy as np


def part1():
    puzzle_input = 36000000
    max_number = puzzle_input // 10
    houses = np.zeros(max_number + 1)
    for i in range(1, max_number + 1):
        houses[i:max_number:i] += 10 * i
    print(np.where(houses >= puzzle_input)[0][0])


def part2():
    puzzle_input = 36000000
    max_number = puzzle_input // 10
    houses = np.zeros(max_number + 1)
    for i in range(1, max_number + 1):
        houses[i:i * 50:i] += 11 * i
    print(np.where(houses >= puzzle_input)[0][0])