

def part1():
    with open("Input/input3.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    most_common = []
    for i in range(len(input[0])):
        most_common.append(find_most_common(input, i))

    gamma_rate = ""
    epsilon_rate = ""
    for x in most_common:
        if x:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    gamma_rate_base10 = int(gamma_rate, 2)
    epsilon_rate_base10 = int(epsilon_rate, 2)

    print(gamma_rate_base10 * epsilon_rate_base10)


def part2():
    with open("Input/input3.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    remaining_oxygen_generator = input
    remaining_co2_scrubber = input

    i = 0
    while remaining_oxygen_generator and remaining_co2_scrubber:
        if i >= len(input[0]):
            break

        most_common = find_most_common(remaining_oxygen_generator, i)
        least_common = 1 - find_most_common(remaining_co2_scrubber, i)

        if len(remaining_oxygen_generator) != 1:
            remaining_oxygen_generator = [r for r in remaining_oxygen_generator if r[i] == str(most_common)]

        if len(remaining_co2_scrubber) != 1:
            remaining_co2_scrubber = [r for r in remaining_co2_scrubber if r[i] == str(least_common)]

        i += 1

    oxygen_generator_rating_base10 = int(remaining_oxygen_generator[0], 2)
    co2_scrubber_rating_base10 = int(remaining_co2_scrubber[0], 2)

    print(oxygen_generator_rating_base10 * co2_scrubber_rating_base10)


def find_most_common(input, i):
    count = 0
    for line in input:
        count += int(line[i])

    if 2 * count >= len(input):
        return 1

    return 0
