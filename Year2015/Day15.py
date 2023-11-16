import json
import re
from itertools import permutations


def part1(part_2=False):
    with open("./Year2015/Input/input15.txt") as fp:
        input = [x.strip("\n").split(" ") for x in fp.readlines()]

    ingredients = [
        Ingredient(
            x[0].strip(":"),
            int(x[2].strip(",")),
            int(x[4].strip(",")),
            int(x[6].strip(",")),
            int(x[8].strip(",")),
            int(x[10].strip(","))
        ) for x in input
    ]

    combinations_generator = sum_to_k_rec(4, 100)
    length_4_combination = [combination for combination in combinations_generator if len(combination) == len(ingredients)]

    maximum = 0
    for c in length_4_combination:
        calories = sum(c[i] * ingredients[i].calories for i in range(len(ingredients)))
        if part_2 and calories != 500:
            continue

        capacity = max(sum(c[i] * ingredients[i].capacity for i in range(len(ingredients))), 0)
        durability = max(sum(c[i] * ingredients[i].durability for i in range(len(ingredients))), 0)
        flavor = max(sum(c[i] * ingredients[i].flavor for i in range(len(ingredients))), 0)
        texture = max(sum(c[i] * ingredients[i].texture for i in range(len(ingredients))), 0)

        score = capacity * durability * flavor * texture

        if score > maximum:
            maximum = score

    print(maximum)


def part2():
    part1(True)


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


def sum_to_k_rec(n, k):
    if n == 1:
        yield (k,)
    else:
        for x in range(1, k):
            for i in sum_to_k_rec(n - 1, k - x):
                yield (x,) + i



