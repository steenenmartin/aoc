import numpy as np

def part1():
    with open("./Input/input4.txt") as fp:
        lines = fp.readlines()

    reals = 0
    for line in lines:
        line = line.replace("\n", "")
        split_line = line.split("-")

        id = int(split_line[-1].split("[")[0])
        checksum = split_line[-1].split("[")[1].replace("]", "")
        strings = split_line[:-1]

        res = {}

        for string in strings:
            for keys in string:
                res[keys] = res.get(keys, 0) + 1

        real = True
        for c in checksum:
            if c not in res or res[c] != max(res.values()):
                real = False
                break
            res.pop(c)

        if real:
            reals += id

    print(reals)


def part2():
    with open("./Input/input4.txt") as fp:
        lines = fp.readlines()

    reals = 0
    for line in lines:
        line = line.replace("\n", "")
        split_line = line.split("-")

        id = int(split_line[-1].split("[")[0])
        checksum = split_line[-1].split("[")[1].replace("]", "")
        strings = split_line[:-1]

        res = {}

        for string in strings:
            for keys in string:
                res[keys] = res.get(keys, 0) + 1

        real = True
        for c in checksum:
            if c not in res or res[c] != max(res.values()):
                real = False
                break
            res.pop(c)

        if not real:
            continue

        a = ord("a")
        for n in range(1, 26):
            for string in strings:
                new_str = ""
                for c in string:
                    new_str += chr((ord(c) - a + n) % 26 + a)
                print(new_str, id)

        # print(new_str, id)


if __name__ == '__main__':
    part1()
    part2()
