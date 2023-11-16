import numpy as np


def part1():
    with open("./Year2015/Input/input6.txt") as fp:
        inputs = [x.strip("\n").split(" ") for x in fp.readlines()]

    matrix = np.zeros((1000, 1000))

    for input in inputs:
        if input[0] == "toggle":
            x = [int(x) for x in input[1].split(",")]
            y = [int(x) for x in input[3].split(",")]
            matrix[x[0]:y[0]+1, x[1]:y[1]+1] = 1 - matrix[x[0]:y[0]+1, x[1]:y[1]+1]

        elif input[0] == "turn":
            x = [int(x) for x in input[2].split(",")]
            y = [int(x) for x in input[4].split(",")]

            if input[1] == "on":
                matrix[x[0]:y[0]+1, x[1]:y[1]+1] = 1
            elif input[1] == "off":
                matrix[x[0]:y[0]+1, x[1]:y[1]+1] = 0
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError

    matrix = matrix % 2
    print(matrix.sum())


def part2():
    with open("./Year2015/Input/input6.txt") as fp:
        inputs = [x.strip("\n").split(" ") for x in fp.readlines()]

    matrix = np.zeros((1000, 1000))

    for input in inputs:
        if input[0] == "toggle":
            x = [int(x) for x in input[1].split(",")]
            y = [int(x) for x in input[3].split(",")]
            matrix[x[0]:y[0]+1, x[1]:y[1]+1] += 2

        elif input[0] == "turn":
            x = [int(x) for x in input[2].split(",")]
            y = [int(x) for x in input[4].split(",")]

            if input[1] == "on":
                matrix[x[0]:y[0]+1, x[1]:y[1]+1] += 1
            elif input[1] == "off":
                matrix[x[0]:y[0]+1, x[1]:y[1]+1] -= np.where(matrix[x[0]:y[0]+1, x[1]:y[1]+1] > 0, 1, 0)
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError

    print(matrix.sum())
