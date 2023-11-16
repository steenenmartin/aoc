import numpy as np
import math
import pipe

def part1():
    with open("Input/input9.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    score = 0
    for i in range(len(input)):
        line = input[i]
        for j in range(len(line)):
            value = int(line[j])
            if value != 9:
                if try_get(input, 0, 1, i, j) > value:
                    if try_get(input, 0, -1, i, j) > value:
                        if try_get(input, 1, 0, i, j) > value:
                            if try_get(input, -1, 0, i, j) > value:
                                score += 1 + value

    print(score)

def part2():
    with open("Input/input9.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    low_points = dict()
    for i in range(len(input)):
        line = input[i]
        for j in range(len(line)):
            value = int(line[j])
            if value != 9:
                if try_get(input, 0, 1, i, j) > value:
                    if try_get(input, 0, -1, i, j) > value:
                        if try_get(input, 1, 0, i, j) > value:
                            if try_get(input, -1, 0, i, j) > value:
                                low_points[(i,j)] = [(i,j)]

    basin_size = []
    for low_point in low_points:
        prev_len = 0
        while True:
            new_low = [low_point]
            for point in low_points[low_point]:
                if try_get2(input, 0, 1, point[0], point[1]):
                    new_low.append((point[0], point[1] + 1))
                if try_get2(input, 0, -1, point[0], point[1]):
                    new_low.append((point[0], point[1] - 1))
                if try_get2(input, 1, 0, point[0], point[1]):
                    new_low.append((point[0] + 1, point[1]))
                if try_get2(input, -1, 0, point[0], point[1]):
                    new_low.append((point[0] - 1, point[1]))
            low_points[low_point].extend(new_low)
            low_points[low_point] = list(set(low_points[low_point]))
            if len(low_points[low_point]) == prev_len:
                break

            prev_len = len(low_points[low_point])

        basin_size.append(len(low_points[low_point]))
    basin_size = list(reversed(sorted(basin_size)))
    print(basin_size[0] * basin_size[1] * basin_size[2])

def try_get(input, up, right, i, j):
    if not 0 <= i + up < len(input[i]) or not 0 <= j + right < len(input[0]):
        return 10

    return int(input[i + up][j + right])

def try_get2(input, up, right, i, j):
    if not 0 <= i + up < len(input[i]) or not 0 <= j + right < len(input[0]):
        return False

    return int(input[i + up][j + right]) < 9
