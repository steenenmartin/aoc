import numpy as np


def part1():
    with open("./Year2015/Input/input2.txt") as fp:
        inputs = [list(map(int, x.strip('\n').split('x'))) for x in fp.readlines()]

    r = 0
    for input in inputs:
       a1 = input[0] * input[1]
       a2 = input[1] * input[2]
       a3 =  input[0] * input[2]

       r += 2 * (a1 + a2 + a3) + min(a1, a2, a3)

    print(r)


def part2():
    with open("./Year2015/Input/input2.txt") as fp:
        inputs = [list(map(int, x.strip('\n').split('x'))) for x in fp.readlines()]

    r = 0
    for input in inputs:
        perimeters = np.array((
                2 * input[0] + 2 * input[1],
                2 * input[1] + 2 * input[2],
                2 * input[0] + 2 * input[2]
            )
        )

        r += np.min(perimeters)

        r += np.product(input)

    print(r)