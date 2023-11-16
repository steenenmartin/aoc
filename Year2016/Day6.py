import numpy as np
import pandas as pd


def part1():
    with open("./Input/input6.txt") as fp:
        lines = fp.readlines()

    print("".join(pd.DataFrame([[s for s in line.replace("\n", "")] for line in lines]).mode().T.get(0)))


def part2():
    with open("./Input/input6.txt") as fp:
        lines = fp.readlines()

    df = pd.DataFrame([[s for s in line.replace("\n", "")] for line in lines])
    print("".join([df.T.iloc[i].value_counts().index[-1] for i in range(df.shape[1])]))


if __name__ == '__main__':
    part1()
    part2()
