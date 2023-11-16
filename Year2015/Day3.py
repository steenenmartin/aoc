import numpy as np

def part1():
    with open("./Year2015/Input/input3.txt") as fp:
        inputs = fp.readline()

    coords = (0, 0)
    visited = {coords: 1}

    for direction in inputs:
        if direction == '>':
            coords = (coords[0] + 1, coords[1])
        if direction == '<':
            coords = (coords[0] - 1, coords[1])
        if direction == '^':
            coords = (coords[0], coords[1] + 1)
        if direction == 'v':
            coords = (coords[0], coords[1] - 1)

        if coords not in visited:
            visited[coords] = 1
        else:
            visited[coords] += 1

    print(len(visited))


def part2():
    with open("./Year2015/Input/input3.txt") as fp:
        inputs = fp.readline()

    santa_coords = (0, 0)
    robo_santa_coords = (0, 0)
    visited = {santa_coords: 2}

    i = 0
    for direction in inputs:
        if i % 2 == 0:
            if direction == '>':
                santa_coords = (santa_coords[0] + 1, santa_coords[1])
            if direction == '<':
                santa_coords = (santa_coords[0] - 1, santa_coords[1])
            if direction == '^':
                santa_coords = (santa_coords[0], santa_coords[1] + 1)
            if direction == 'v':
                santa_coords = (santa_coords[0], santa_coords[1] - 1)

            if santa_coords not in visited:
                visited[santa_coords] = 1
            else:
                visited[santa_coords] += 1
        else:
            if direction == '>':
                robo_santa_coords = (robo_santa_coords[0] + 1, robo_santa_coords[1])
            if direction == '<':
                robo_santa_coords = (robo_santa_coords[0] - 1, robo_santa_coords[1])
            if direction == '^':
                robo_santa_coords = (robo_santa_coords[0], robo_santa_coords[1] + 1)
            if direction == 'v':
                robo_santa_coords = (robo_santa_coords[0], robo_santa_coords[1] - 1)

            if robo_santa_coords not in visited:
                visited[robo_santa_coords] = 1
            else:
                visited[robo_santa_coords] += 1

        i += 1

    print(len(visited))