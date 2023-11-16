import json
import re
from itertools import permutations


def part1():
    with open("./Year2015/Input/input14.txt") as fp:
        input = [x.strip("\n").split(" ") for x in fp.readlines()]

    reindeers = [Reindeer(x[0], int(x[3]), int(x[6]), int(x[-2])) for x in input]

    for i in range(2503):
        for reindeer in reindeers:
            reindeer.move()

    print(max([r.distance for r in reindeers]))


def part2():
    with open("./Year2015/Input/input14.txt") as fp:
        input = [x.strip("\n").split(" ") for x in fp.readlines()]

    reindeers = [Reindeer(x[0], int(x[3]), int(x[6]), int(x[-2])) for x in input]

    for i in range(2503):
        for reindeer in reindeers:
            reindeer.move()
        max_dist = max([r.distance for r in reindeers])

        winning_deer = [r for r in reindeers if r.distance == max_dist]
        for deer in winning_deer:
            deer.points += 1

    print(max([r.points for r in reindeers]))


class Reindeer:
    def __init__(self, name, velocity, endurance, rest_period):
        self.name = name
        self.velocity = velocity
        self.endurance = endurance
        self.rest_period = rest_period

        self.distance = 0
        self.remaining_endurance = endurance
        self.rest_elapsed = 0
        self.points = 0

    def move(self):
        if self.remaining_endurance > 0:
            self.fly()
        else:
            self.rest()

    def fly(self):
        self.distance += self.velocity
        self.remaining_endurance -= 1

    def rest(self):
        self.rest_elapsed += 1

        if self.rest_elapsed == self.rest_period:
            self.rest_elapsed = 0
            self.remaining_endurance = self.endurance




