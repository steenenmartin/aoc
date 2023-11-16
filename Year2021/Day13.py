import itertools
from collections import Counter

import numpy as np


def part1():

    with open("Input/input13.txt") as fp:
        coords = []
        folds = []
        while True:
            line = fp.readline()
            if not line:
                break

            if line == "\n":
                continue
            elif line.startswith("fold along y"):
                folds.append(["y", int(line.strip("\n").split("=")[1])])
            elif line.startswith("fold along x"):
                folds.append(["x", int(line.strip("\n").split("=")[1])])
            else:
                coords.append([int(x) for x in line.strip("\n").split(",")])
        max_y = max(y[1] for y in coords) + 1
        max_x = max(x[0] for x in coords) + 1

        matrix = np.zeros((max_y, max_x))

        for coord in coords:
            matrix[coord[1], coord[0]] += 1

        new_matrix = matrix
        for fold in folds:
            if fold[0] == "y":
                new_matrix = new_matrix[0:fold[1],]
                for y in range(fold[1], matrix.shape[0]):
                    for x in range(matrix.shape[1]):
                        new_matrix[fold[1] - y, x] += matrix[y, x]
            else:
                new_matrix = new_matrix[:,0:fold[1]]
                for y in range(matrix.shape[0]):
                    for x in range(fold[1], matrix.shape[1]):
                        new_matrix[y, fold[1] - x] += matrix[y, x]

            matrix = np.where(new_matrix != 0, 1, 0)

            print(matrix.sum())

        print(matrix)






