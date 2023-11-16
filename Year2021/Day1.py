

def part1():
    increasing_depth_count = 0
    with open("Input/input1.txt") as fp:
        previous_depth = 1e100
        while True:
            line = fp.readline()

            if not line:
                break

            depth = int(line)
            if depth > previous_depth:
                increasing_depth_count += 1

            previous_depth = depth

    print(increasing_depth_count)

def part2():
    with open("Input/input1.txt") as fp:
        depths = [int(x) for x in fp.readlines()]

    previous_three_measurement = 1e100
    increasing_three_measurement_depth_count = 0

    for i in range(2, len(depths)):
        three_measurement = depths[i] + depths[i-1] + depths[i-2]

        if three_measurement > previous_three_measurement:
            increasing_three_measurement_depth_count += 1

        previous_three_measurement = three_measurement

    print(increasing_three_measurement_depth_count)