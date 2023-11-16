import numpy as np


def part1():
    with open("./Input/input3.txt") as fp:
        lines = fp.readlines()

    triangles = [[int(y) for y in x.split()] for x in lines]

    valid_triangles = 0
    for triangle in triangles:
        if triangle[0] + triangle[1] > triangle[2] and triangle[1] + triangle[2] > triangle[0] and triangle[0] + triangle[2] > triangle[1]:
            valid_triangles += 1

    print(valid_triangles)


def part2():
    with open("./Input/input3.txt") as fp:
        lines = fp.readlines()

    triangles = []
    t1 = []
    t2 = []
    t3 = []
    for i in range(len(lines)):
        if len(t1) == len(t2) == len(t3) == 3:
            triangles.append(t1)
            triangles.append(t2)
            triangles.append(t3)
            t1 = []
            t2 = []
            t3 = []

        triangle_entries = [int(x) for x in lines[i].split()]
        t1.append(triangle_entries[0])
        t2.append(triangle_entries[1])
        t3.append(triangle_entries[2])

    triangles.append(t1)
    triangles.append(t2)
    triangles.append(t3)

    valid_triangles = 0
    for triangle in triangles:
        if triangle[0] + triangle[1] > triangle[2] and triangle[1] + triangle[2] > triangle[0] and triangle[0] + triangle[2] > triangle[1]:
            valid_triangles += 1

    print(valid_triangles)


if __name__ == '__main__':
    part1()
    part2()
