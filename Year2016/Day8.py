from copy import deepcopy
import numpy as np


def part1():
    with open(".\input8.txt") as f:
        input = f.readlines()

    rows = 6
    cols = 50
    m = np.zeros((rows, cols))

    for i in input:
        i_split = i.replace("\n", "").split(" ")
        if i_split[0] == "rect":
            x, y = (int(i_split[1].split("x")[0]), int(i_split[1].split("x")[1]))
            m[:y, :x] = 1
        elif i_split[0] == "rotate":
            rotate_row = i_split[1] == "row"
            rotate_col = not rotate_row
            index = int(i_split[2].split("=")[1])
            by = int(i_split[-1])

            if rotate_row:
                row = deepcopy(m)[index, :]
                for x in range(cols):
                    new_index = (x + by) % cols
                    m[index, new_index] = row[x]
            if rotate_col:
                col = deepcopy(m)[:, index]
                for y in range(rows):
                    new_index = (y + by) % rows
                    m[new_index, index] = col[y]

    print(m.sum())

    for i in range(rows):
        s = ""
        for j in range(cols):
            if m[i, j] == 1:
                s += "##"
            else:
                s += "  "
        print(s)  # EFEYKFRFIJ


def part2():
    print()


if __name__ == "__main__":
    part1()
    part2()
