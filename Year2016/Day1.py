import numpy as np


def part1():
    with open("./Year2016/Input/input1.txt") as fp:
        inputs = fp.read().split(", ")

    face = np.matrix([[0], [1]])
    coords = (0, 0)

    for i in inputs:
        length = int(i[1:])
        if i.startswith("R"):
            face = np.matrix([[0, 1], [-1, 0]]) * face
        elif i.startswith("L"):
            face = np.matrix([[0, -1], [1, 0]]) * face
        else:
            raise NotImplementedError

        coords = (int(coords[0] + length * face[0]), int(coords[1] + length * face[1]))

    print(sum(abs(c) for c in coords))


def part2():
    with open("./Year2016/Input/input1.txt") as fp:
        inputs = fp.read().split(", ")

    face = np.matrix([[0], [1]])
    coords = (0, 0)
    visited_twice_coords = None
    visited_coords = []

    for i in inputs:
        length = int(i[1:])
        if i.startswith("R"):
            face = np.matrix([[0, 1], [-1, 0]]) * face
        elif i.startswith("L"):
            face = np.matrix([[0, -1], [1, 0]]) * face
        else:
            raise NotImplementedError

        prev_coords = coords
        coords = (int(coords[0] + length * face[0]), int(coords[1] + length * face[1]))

        first = True
        for x in range(prev_coords[0], coords[0] + 1, 1 if coords[0] >= prev_coords[0] else -1):
            for y in range(prev_coords[1], coords[1] + 1, 1 if coords[1] >= prev_coords[1] else -1):
                if (x, y) in visited_coords:
                    if first:
                        first = False
                        continue
                    else:
                        visited_twice_coords = (x, y)
                else:
                    visited_coords.append((x, y))

        if visited_twice_coords is not None:
            break

    print(sum(abs(c) for c in visited_twice_coords))