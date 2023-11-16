

def part1():
    with open("./Year2015/Input/input1.txt") as fp:
        inputs = fp.readlines()

    sum = 0
    for char in inputs[0]:
        if char == "(":
            sum += 1
        elif char == ")":
            sum -= 1
        else:
            raise NotImplementedError(f"Did not recognize char {char}")

    print(sum)


def part2():
    with open("./Year2015/Input/input1.txt") as fp:
        inputs = fp.readlines()

    pos = 0
    sum = 0
    for char in inputs[0]:
        if sum == -1:
            break

        if char == "(":
            sum += 1
        elif char == ")":
            sum -= 1
        else:
            raise NotImplementedError(f"Did not recognize char {char}")

        pos += 1

    print(pos)


if __name__ == '__main__':
    part1()
    part2()