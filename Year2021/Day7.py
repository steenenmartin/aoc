import numpy as np
import math

def part1():
    with open("Input/input7.txt") as fp:
        distances = [int(distance) for distance in fp.readline().split(",")]

        fuel_consumptions = []
        for d in range(min(distances), max(distances)):
            s = 0
            for distance in distances:
                s += abs(d - distance)

            fuel_consumptions.append(s)

        print(min(fuel_consumptions))


def part2():
    with open("Input/input7.txt") as fp:
        distances = [int(distance) for distance in fp.readline().split(",")]

        fuel_consumptions = []
        for alignment_position in range(min(distances), max(distances) + 1):
            consumption = 0
            for distance in distances:
                alignment_distance = abs(alignment_position - distance)
                consumption += (alignment_distance ** 2 + alignment_distance) / 2

            fuel_consumptions.append(consumption)

        print(min(fuel_consumptions))