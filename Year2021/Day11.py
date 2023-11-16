import numpy as np


def part1():
    with open("Input/input11.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]
    n = len(input)
    m = len(input[0])
    matrix = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            matrix[i, j] = input[i][j]

    s = 0
    for step in range(100):
        for i in range(n):
            for j in range(m):
                increase(matrix, i, j)

        flashes = np.where(matrix == 10, 1, 0)

        s += flashes.sum()

        matrix -= flashes * 10

    print(s)


def part2():
    with open("Input/input11.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    n = len(input)
    m = len(input[0])
    matrix = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            matrix[i, j] = input[i][j]

    step = 0
    while True:
        if matrix.sum() == 0:
            print(step)
            break

        for i in range(n):
            for j in range(m):
                increase(matrix, i, j)

        flashes = np.where(matrix == 10, 1, 0)
        matrix -= flashes * 10

        step += 1


def increase(matrix, i, j):
    if 0 <= i < matrix.shape[0] and 0 <= j < matrix.shape[1]:
        if matrix[i, j] != 10:
            matrix[i, j] += 1

            if matrix[i, j] == 10:
                flash(matrix, i, j)


def flash(matrix, i, j):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if not x == y == 0:
                increase(matrix, i + x, j + y)
