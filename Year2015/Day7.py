

def part1():
    with open("./Year2015/Input/input7.txt") as fp:
        input = [x.strip("\n").split(" ") for x in fp.readlines()]

    def bit_not(n, numbits=16):
        return (1 << numbits) - 1 - n

    values = dict()
    while input:
        for line in input:
            if (line[0] in values or line[0].isdigit()) and len(line) == 3:
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                values[line[-1]] = x
                input.remove(line)
            if "NOT" in line and (line[1] in values or line[1].isdigit()):
                if line[1].isdigit():
                    x = int(line[1])
                else:
                    x = values[line[1]]

                values[line[-1]] = bit_not(x)
                input.remove(line)
            if "AND" in line and (line[0] in values or line[0].isdigit()) and (line[2] in values or line[2].isdigit()):
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                if line[2].isdigit():
                    y = int(line[2])
                else:
                    y = values[line[2]]

                values[line[-1]] = x & y
                input.remove(line)
            if "OR" in line and (line[0] in values or line[0].isdigit()) and (line[2] in values or line[2].isdigit()):
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                if line[2].isdigit():
                    y = int(line[2])
                else:
                    y = values[line[2]]

                values[line[-1]] = x | y
                input.remove(line)
            if "RSHIFT" in line and (line[0] in values or line[0].isdigit()) and (line[2] in values or line[2].isdigit()):
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                if line[2].isdigit():
                    y = int(line[2])
                else:
                    y = values[line[2]]

                values[line[-1]] = x >> y
                input.remove(line)

            if "LSHIFT" in line and (line[0] in values or line[0].isdigit()) and (line[2] in values or line[2].isdigit()):
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                if line[2].isdigit():
                    y = int(line[2])
                else:
                    y = values[line[2]]

                values[line[-1]] = x << y
                input.remove(line)

    print(values["a"])


def part2():
    with open("./Year2015/Input/input7.txt") as fp:
        input = [x.strip("\n").split(" ") for x in fp.readlines()]

    def bit_not(n, numbits=16):
        return (1 << numbits) - 1 - n

    values = {'b': 46065}
    while input:
        for line in input:
            if line == ['1674', '->', 'b']:
                input.remove(line)
                continue
            if (line[0] in values or line[0].isdigit()) and len(line) == 3:
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                values[line[-1]] = x
                input.remove(line)
            if "NOT" in line and (line[1] in values or line[1].isdigit()):
                if line[1].isdigit():
                    x = int(line[1])
                else:
                    x = values[line[1]]

                values[line[-1]] = bit_not(x)
                input.remove(line)
            if "AND" in line and (line[0] in values or line[0].isdigit()) and (line[2] in values or line[2].isdigit()):
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                if line[2].isdigit():
                    y = int(line[2])
                else:
                    y = values[line[2]]

                values[line[-1]] = x & y
                input.remove(line)
            if "OR" in line and (line[0] in values or line[0].isdigit()) and (line[2] in values or line[2].isdigit()):
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                if line[2].isdigit():
                    y = int(line[2])
                else:
                    y = values[line[2]]

                values[line[-1]] = x | y
                input.remove(line)
            if "RSHIFT" in line and (line[0] in values or line[0].isdigit()) and (line[2] in values or line[2].isdigit()):
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                if line[2].isdigit():
                    y = int(line[2])
                else:
                    y = values[line[2]]

                values[line[-1]] = x >> y
                input.remove(line)

            if "LSHIFT" in line and (line[0] in values or line[0].isdigit()) and (line[2] in values or line[2].isdigit()):
                if line[0].isdigit():
                    x = int(line[0])
                else:
                    x = values[line[0]]

                if line[2].isdigit():
                    y = int(line[2])
                else:
                    y = values[line[2]]

                values[line[-1]] = x << y
                input.remove(line)

    print(values["a"])

