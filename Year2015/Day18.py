import math
from itertools import combinations

import pandas as pd
import numpy as np


def part1():
    with open("./Year2015/Input/input18.txt") as fp:
        input = [list(x.strip("\n")) for x in fp.readlines()]

    df = pd.DataFrame(input)
    matrix = np.where(df == "#", 1, 0)

    for n in range(100):
        print(n)
        next_matrix = np.zeros_like(matrix)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                adjacent_entries = adj_finder(matrix, (i, j))
                if matrix[i, j] == 1:
                    if 2 <= sum(matrix[adj[0], adj[1]] for adj in adjacent_entries) <= 3:
                        next_matrix[i, j] = 1
                    else:
                        next_matrix[i, j] = 0
                else:
                    next_matrix[i, j] = 1 if sum(matrix[adj[0], adj[1]] for adj in adjacent_entries) == 3 else 0

        matrix = next_matrix

    print(np.sum(matrix))


def part2():
    with open("./Year2015/Input/input18.txt") as fp:
        input = [list(x.strip("\n")) for x in fp.readlines()]

    df = pd.DataFrame(input)
    matrix = np.where(df == "#", 1, 0)
    for i in [0, matrix.shape[0] - 1]:
        for j in [0, matrix.shape[1] - 1]:
            matrix[i, j] = 1

    for n in range(100):
        print(n)
        next_matrix = np.zeros_like(matrix)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if i in [0, matrix.shape[0] - 1] and j in [0, matrix.shape[1] - 1]:
                    next_matrix[i, j] = 1
                    continue

                adjacent_entries = adj_finder(matrix, (i, j))
                if matrix[i, j] == 1:
                    if 2 <= sum(matrix[adj[0], adj[1]] for adj in adjacent_entries) <= 3:
                        next_matrix[i, j] = 1
                    else:
                        next_matrix[i, j] = 0
                else:
                    next_matrix[i, j] = 1 if sum(matrix[adj[0], adj[1]] for adj in adjacent_entries) == 3 else 0

        matrix = next_matrix

    print(np.sum(matrix))


def adj_finder(matrix, position):
    adj = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            range_x = range(0, matrix.shape[0])
            range_y = range(0, matrix.shape[1])

            (newX, newY) = (position[0] + dx, position[1] + dy)

            if (newX in range_x) and (newY in range_y) and (dx, dy) != (0, 0):
                adj.append((newX, newY))

    return adj
