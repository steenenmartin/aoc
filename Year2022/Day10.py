import numpy as np


with open("./Input/input10.txt") as f:
    unfinished_cycles = [0]
    cycle_values = [1]

    for line in f.readlines():
        line = line.strip("\n")

        if line.startswith("addx"):
            unfinished_cycles = [int(line.split(" ")[-1]), 0] + unfinished_cycles
        elif line == "noop":
            unfinished_cycles = [0] + unfinished_cycles

        if unfinished_cycles:
            value = unfinished_cycles.pop()
        else:
            value = 0

        cycle_values.append(cycle_values[-1] + value)

    while unfinished_cycles:
        cycle_values.append(cycle_values[-1] + unfinished_cycles.pop())

    print("p1", sum([i * cycle_values[i] for i in [20, 60, 100, 140, 180, 220]]))

    display = np.zeros((6, 40))
    cycle = 1
    for i in range(display.shape[0]):
        for j in range(display.shape[1]):
            sprite_center = cycle_values[cycle]

            if sprite_center - 1 <= j <= sprite_center + 1:
                display[i, j] = 1

            cycle += 1

    for i in range(display.shape[0]):
        s = ""
        for j in range(display.shape[1]):
            s += "###" if display[i, j] else "   "
        print(f"{s}")






