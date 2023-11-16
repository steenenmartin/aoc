

def part1():
    with open("Input/input2.txt") as fp:
        inputs = [[x.split(" ")[0], int(x.split(" ")[1])] for x in fp.readlines()]

    horizontal = 0
    vertical = 0
    for input in inputs:
        if input[0] == "forward":
            horizontal += input[1]
        elif input[0] == "up":
            vertical -= input[1]
        elif input[0] == "down":
            vertical += input[1]
        else:
            raise ValueError

    print(horizontal * vertical)

def part2():
    with open("Input/input2.txt") as fp:
        inputs = [[x.split(" ")[0], int(x.split(" ")[1])] for x in fp.readlines()]

    horizontal = 0
    vertical = 0
    aim = 0
    for input in inputs:
        if input[0] == "forward":
            horizontal += input[1]
            vertical += aim * input[1]
        elif input[0] == "up":
            aim -= input[1]
        elif input[0] == "down":
            aim += input[1]
        else:
            raise ValueError

    print(horizontal * vertical)