import json
import re
from itertools import permutations


def part1():
    with open("./Year2015/Input/input13.txt") as fp:
        input = [x.strip("\n").split(" ") for x in fp.readlines()]

    person_1s = [x[0] for x in input]
    person_2s = [x[-1].strip(".") for x in input]

    happiness_map = {(x[0], x[-1].strip(".")): int(x[3]) * (-1 if x[2] == "lose" else 1) for x in input}

    persons = set(person_1s).intersection(set(person_2s))

    perms = list(permutations(persons))

    max_happines = 0
    for p in perms:
        happiness = 0
        for i in range(len(p) - 1):
            happiness += happiness_map[p[i], p[i + 1]]
            happiness += happiness_map[p[i + 1], p[i]]

        happiness += happiness_map[p[0], p[-1]]
        happiness += happiness_map[p[-1], p[0]]

        if happiness > max_happines:
            max_happines = happiness

    print(max_happines)


def part2():
    with open("./Year2015/Input/input13.txt") as fp:
        input = [x.strip("\n").split(" ") for x in fp.readlines()]

    person_1s = [x[0] for x in input]
    person_2s = [x[-1].strip(".") for x in input]

    happiness_map = {(x[0], x[-1].strip(".")): int(x[3]) * (-1 if x[2] == "lose" else 1) for x in input}

    persons = set(person_1s).intersection(set(person_2s))

    for person in persons:
        happiness_map[(person, "Martin")] = 0
        happiness_map[("Martin", person)] = 0

    persons.add("Martin")

    perms = list(permutations(persons))

    max_happines = 0
    for p in perms:
        happiness = 0
        for i in range(len(p) - 1):
            happiness += happiness_map[p[i], p[i + 1]]
            happiness += happiness_map[p[i + 1], p[i]]

        happiness += happiness_map[p[0], p[-1]]
        happiness += happiness_map[p[-1], p[0]]

        if happiness > max_happines:
            max_happines = happiness

    print(max_happines)




