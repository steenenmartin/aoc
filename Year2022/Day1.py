

def part1():
    elves = {}
    with open("./Year2022/Input/input1.txt") as f:
        i = 0
        inventory = []
        for line in f.readlines():
            line = line.strip("\n")

            if line != "":
                inventory.append(int(line))
            else:
                elves[i] = inventory
                inventory = []
                i += 1
        sums = [sum(x) for x in elves.values()]
        print(max(sums))


def part2():
    elves = {}
    with open("./Year2022/Input/input1.txt") as f:
        i = 0
        inventory = []
        for line in f.readlines():
            line = line.strip("\n")

            if line != "":
                inventory.append(int(line))
            else:
                elves[i] = inventory
                inventory = []
                i += 1
        sums = sorted([sum(x) for x in elves.values()], reverse=True)
        print(sums[0] + sums[1] + sums[2])