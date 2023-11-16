

def part1():
    with open("./Input/input3.txt") as f:
        sum = 0
        for s in f.readlines():
            s = s.strip("\n")

            first_half = set(s[:len(s) // 2])
            second_half = set(s[len(s) // 2:])

            common = first_half.intersection(second_half)

            for c in common:
                if c.islower():
                    sum += ord(c) - 96
                else:
                    sum += ord(c) - 64 + 26

        print(sum)


def part2():
    with open("./Input/input3.txt") as f:
        input = [x.strip("\n") for x in f.readlines()]

    groups = [input[n:n + 3] for n in range(0, len(input), 3)]
    sum = 0
    for g in groups:
        common = None
        for s in g:
            common = set(s) if common is None else common.intersection(set(s))

        for c in common:
            if c.islower():
                sum += ord(c) - 96
            else:
                sum += ord(c) - 64 + 26

    print(sum)


if __name__ == "__main__":
    part1()
    part2()
