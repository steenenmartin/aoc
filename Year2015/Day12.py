import json
import re


def part1():
    with open("./Year2015/Input/input12.txt") as fp:
        input = fp.readlines()

        integers = re.findall("[-\d]+", input[0])

        print(sum(int(x) for x in integers))


def part2():
    with open("./Year2015/Input/input12.txt") as fp:
        input = fp.readlines()

    input_json = json.loads(input[0])

    sum = recurse(input_json)

    print(sum)


def recurse(obj):
    sum = 0
    if isinstance(obj, dict):
        if "red" not in obj.values():
            for val in obj.values():
                sum += recurse(val)
    elif isinstance(obj, list):
        for val in obj:
            sum += recurse(val)
    elif isinstance(obj, int):
        return obj

    return sum


