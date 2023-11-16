

def part1():
    with open("./Year2015/Input/input16.txt") as fp:
        input = [
            {
                x.strip("\n").split(" ")[2].strip(":"): int(x.strip("\n").split(" ")[3].strip(",")),
                x.strip("\n").split(" ")[4].strip(":"): int(x.strip("\n").split(" ")[5].strip(",")),
                x.strip("\n").split(" ")[6].strip(":"): int(x.strip("\n").split(" ")[7].strip(",")),
            } for x in fp.readlines()]

    scan = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    dicct = {}
    for i in range(len(input)):
        x = input[i]
        breaker = False
        for key in x.keys():
            if key in x:
                if scan[key] != x[key]:
                    dicct[i] = False
                    breaker = True
                    break

        if not breaker:
            dicct[i] = True

    [true] = [k for k in dicct.keys() if dicct[k] == True]
    print(true + 1)


def part2():
    with open("./Year2015/Input/input16.txt") as fp:
        input = [
            {
                x.strip("\n").split(" ")[2].strip(":"): int(x.strip("\n").split(" ")[3].strip(",")),
                x.strip("\n").split(" ")[4].strip(":"): int(x.strip("\n").split(" ")[5].strip(",")),
                x.strip("\n").split(" ")[6].strip(":"): int(x.strip("\n").split(" ")[7].strip(",")),
            } for x in fp.readlines()]

    scan = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    dicct = {}
    for i in range(len(input)):
        x = input[i]
        breaker = False
        for key in x.keys():
            if key in x:
                if key in ("trees", "cats"):
                    if scan[key] >= x[key]:
                        dicct[i] = False
                        breaker = True
                        break
                elif key in ("pomeranians", "goldfish"):
                    if scan[key] <= x[key]:
                        dicct[i] = False
                        breaker = True
                        break
                elif scan[key] != x[key]:
                    dicct[i] = False
                    breaker = True
                    break

        if not breaker:
            dicct[i] = True

    [true] = [k for k in dicct.keys() if dicct[k] == True]
    print(true + 1)

