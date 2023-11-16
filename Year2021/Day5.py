import numpy as np


def part1(no_diagonals=False):
    with open("Input/input5.txt") as fp:
        line_segments = [
            LineSegment(
                Point(
                    int(x.strip("\n").strip(" ").split("->")[0].split(",")[0]),
                    int(x.strip("\n").strip(" ").split("->")[0].split(",")[1])),
                Point(
                    int(x.strip("\n").strip(" ").split("->")[1].split(",")[0]),
                    int(x.strip("\n").strip(" ").split("->")[1].split(",")[1]))
            ) for x in fp.readlines()]

    x_max = max(max(s.from_point.x, s.to_point.x) for s in line_segments)
    y_max = max(max(s.from_point.y, s.to_point.y) for s in line_segments)

    matrix = np.zeros((x_max + 1, y_max + 1))
    for line_segment in line_segments:
        if no_diagonals:
            if not (line_segment.from_point.x == line_segment.to_point.x or line_segment.from_point.y == line_segment.to_point.y):
                continue

        x1 = line_segment.from_point.x
        x2 = line_segment.to_point.x

        y1 = line_segment.from_point.y
        y2 = line_segment.to_point.y

        x = x1
        y = y1
        matrix[x, y] += 1
        reached_end_point = False

        while not reached_end_point:
            if x != x2:
                x += 1 if x2 > x1 else -1

            if y != y2:
                y += 1 if y2 > y1 else -1

            matrix[x, y] += 1

            if x == x2 and y == y2:
                reached_end_point = True

    print(np.where(matrix >= 2, 1, 0).sum())


def part2():
    part1(no_diagonals=False)


class LineSegment:
    def __init__(self, from_point, to_point):
        self.from_point = from_point
        self.to_point = to_point


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
