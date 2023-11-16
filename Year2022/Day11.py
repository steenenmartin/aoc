from dataclasses import dataclass
from typing import Callable
import numpy as np
import math


@dataclass(frozen=False)
class Monkey:
    number: np.dtype('int64').type
    items: list[int]
    operator: Callable
    divisor: np.dtype('int64').type
    test: Callable
    inspections = 0


def solve(worry_level_divisor, rounds):
    with open("./Input/input11.txt") as f:
        monkeys = []
        for line in f.readlines():
            line = line.strip("\n")
            line = line.lstrip(" ")
            if line.startswith("Monkey"):
                number = np.dtype('int64').type(line.split(" ")[-1].strip(":"))
            elif line.startswith("Starting items:"):
                items = [np.dtype('int64').type(i.strip(",")) for i in line.split(" ")[2:]]
            elif line.startswith("Operation"):
                if line.split(" ")[-2] == "*":
                    if line.split(" ")[-1].isdigit():
                        integer = np.dtype('int64').type(line.split(" ")[-1])
                        operation = lambda x, n=integer: x * n
                    elif line.split(" ")[-1] == "old":
                        operation = lambda x: np.multiply(x, x)
                    else:
                        raise NotImplementedError
                elif line.split(" ")[-2] == "+":
                    if line.split(" ")[-1].isdigit():
                        integer = np.dtype('int64').type(line.split(" ")[-1])
                        operation = lambda x, n=integer: x + n
                    elif line.split(" ")[-1] == "old":
                        operation = lambda x: x + x
                    else:
                        raise NotImplementedError
            elif line.startswith("Test"):
                divisible_by = np.dtype('int64').type(line.split(" ")[-1])
            elif line.startswith("If true"):
                test_true = np.dtype('int64').type(line.split(" ")[-1])
            elif line.startswith("If false"):
                test_false = np.dtype('int64').type(line.split(" ")[-1])
            elif line == "":
                monkeys.append(
                    Monkey(
                        number,
                        items,
                        operation,
                        divisible_by,
                        lambda x, t=test_true, f=test_false, d=divisible_by: t if x % d == 0 else f
                    )
                )
            else:
                raise NotImplementedError

        divisor_limit = np.prod([m.divisor for m in monkeys])

        for i in range(rounds):
            for monkey in monkeys:
                for item in monkey.items:
                    monkey.inspections += 1

                    worry_level = monkey.operator(item)
                    worry_level = math.floor(worry_level / worry_level_divisor) if worry_level_divisor != 1 else worry_level
                    worry_level %= divisor_limit
                    [new_monkey] = [m for m in monkeys if m.number == monkey.test(worry_level)]
                    new_monkey.items.append(worry_level)
                    monkey.items = monkey.items[1:]

        return list(sorted([x.inspections for x in monkeys]))[-2:]


if __name__ == "__main__":
    print("p1", solve(3, 20))
    print("p2", solve(1, 10000))
