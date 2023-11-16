

def part1():
    with open("./Input/input4.txt") as f:
        sum = 0
        for s in f.readlines():
            pairs = [(int(ss.split("-")[0]), int(ss.split("-")[1])) for ss in s.strip("\n").split(",")]

            if pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][1] or pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]:
                sum += 1

        print(sum)


def part2():
    with open("./Input/input4.txt") as f:
        sum = 0
        for s in f.readlines():
            pairs = [(int(ss.split("-")[0]), int(ss.split("-")[1])) for ss in s.strip("\n").split(",")]

            if (
                pairs[1][0] <= pairs[0][0] <= pairs[1][1] or
                pairs[1][0] <= pairs[0][1] <= pairs[1][1] or
                pairs[0][0] <= pairs[1][0] <= pairs[0][1] or
                pairs[0][0] <= pairs[1][1] <= pairs[0][1]
            ):
                sum += 1

        print(sum)

if __name__ == "__main__":
    part1()
    part2()
