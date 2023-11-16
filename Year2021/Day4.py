import pandas as pd
import numpy as np


def part1():
    draws, df_list, new_df = parse_input()

    counting_dfs = [pd.DataFrame(np.zeros((df.shape[0], df.shape[1]))) for df in df_list]
    breaker = False
    for draw in draws:
        for x in range(len(df_list)):
            df = df_list[x]
            counting_dfs[x] = counting_dfs[x].add(df.isin([draw]), fill_value=0)

            if any(x for x in counting_dfs[x].all(axis=0)) or any(x for x in counting_dfs[x].all(axis=1)):
                score = (df_list[x] * (1 - counting_dfs[x])).to_numpy().sum() * draw
                print(score)
                breaker = True

            if breaker:
                break

        if breaker:
            break


def part2():
    draws, df_list, new_df = parse_input()

    counting_dfs = [pd.DataFrame(np.zeros((df.shape[0], df.shape[1]))) for df in df_list]
    win = np.zeros(len(df_list))
    for draw in draws:
        for x in range(len(df_list)):
            if win[x]:
                continue

            df = df_list[x]
            counting_dfs[x] = counting_dfs[x].add(df.isin([draw]), fill_value=0)

            if any(x for x in counting_dfs[x].all(axis=0)) or any(x for x in counting_dfs[x].all(axis=1)):
                score = (df_list[x] * (1 - counting_dfs[x])).to_numpy().sum() * draw
                win[x] = 1

            if sum(1-win) == 0:
                print(score)


def parse_input():
    with open("Input/input4.txt") as fp:
        draws = [int(x.strip("\n")) for x in fp.readline().split(",")]
        fp.readline()

        df_list = []
        new_df = pd.DataFrame()
        for line in fp.readlines():
            if line == "\n":
                df_list.append(new_df)
                new_df = pd.DataFrame()

            return draws, df_list, new_df.append(pd.DataFrame([int(x) for x in line.strip("\n").split(" ") if x != ""]).T, ignore_index=True)