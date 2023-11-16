import numpy as np


def part1(m, initial):
    with open("./Input/input2.txt") as fp:
        inputs = fp.readlines()

    max_index = m.shape[0] - 1

    i, j = initial
    for line in inputs:
        for c in line:
            if c == "R":
                if j < max_index and m[i, j + 1]:
                    j += 1
            if c == "L":
                if j > 0 and m[i, j - 1]:
                    j -= 1
            if c == "U":
                if i > 0 and m[i - 1, j]:
                    i -= 1
            if c == "D":
                if i < max_index and m[i + 1, j]:
                    i += 1

        print(m[i, j])

    print("")


if __name__ == '__main__':
    m1 = np.matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    part1(m1, (1, 1))

    m2 = np.matrix([
        [0,  0,  1,  0, 0],
        [0,  2,  3,  4, 0],
        [5,  6,  7,  8, 9],
        [0, 10, 11, 12, 0],
        [0,  0, 13,  0, 0]
    ])
    part1(m2, (2, 0))
