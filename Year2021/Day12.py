import itertools


def part1():
    with open("Input/input12.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

        caves = [x.split("-") for x in input]
        caves = list(set(itertools.chain(*caves)))
        caves = [Cave(x, x.lower() == x) for x in caves]

        for connection in input:
            connected_caves = [Cave(x, x.lower() == x) for x in connection.split("-")]

            for i in range(2):
                [c.add_adjecent_cave(connected_caves[1 - i]) for c in caves if c.name == connected_caves[i].name]

        string_list = dict()
        search(caves, [c for c in caves if c.name == "start"][0], string_list)
        print(len(string_list))


def search(caves, start, string_list, build_string=","):
    build_string_list = build_string.split(",")
    counters = {x: build_string_list.count(x) for x in build_string_list if x != ""}

    if ("start" in counters and start.name == "start") or ("end" in counters and start.name == "end"):
        return

    if start.is_small and start.name in counters and counters[start.name] == 2:
        return

    if any(x.lower() == x and counters[x] == 2 and start.name != x for x in counters) and start.is_small and start.name in counters:
        return

    build_string += start.name + ","

    # for counter in counters:
    #     if counter.lower() == counter and counters[counter] > 1:
    #         return

    if start.name == "end":
        string_list[build_string] = 0
        return

    for c in start.adjecent_caves:
        cc = [ccc for ccc in caves if ccc.name == c.name][0]
        search(caves, cc, string_list, build_string)


class Cave:
    def __init__(self, name, is_small):
        self.counter = 0
        self.name = name
        self.is_small = is_small
        self.adjecent_caves = []

    def add_adjecent_cave(self, cave):
        self.adjecent_caves.append(cave)
        self.adjecent_caves = list(set(self.adjecent_caves))

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)






