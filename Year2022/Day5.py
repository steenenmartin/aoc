

def part1(cratemover_version=9000):
    h1 = ["M", "J", "C", "B", "F", "R", "L", "H"]
    h2 = ["Z", "C", "D"]
    h3 = ["H", "J", "F", "C", "N", "G", "W"]
    h4 = ["P", "J", "D", "M", "T", "S", "B"]
    h5 = ["N", "C", "D", "R", "J"]
    h6 = ["W", "L", "D", "Q", "P", "J", "G", "Z"]
    h7 = ["P", "Z", "T", "F", "R", "H"]
    h8 = ["L", "V", "M", "G"]
    h9 = ["C", "B", "G", "P", "F", "Q", "R", "J"]

    heaps = [h1, h2, h3, h4, h5, h6, h7, h8, h9]

    with open("./Input/input5.txt") as f:
        for line in f.readlines():
            line = line.split()

            move_n = int(line[1])
            move_from = int(line[3])
            move_to = int(line[5])

            popped = heaps[move_from - 1][-move_n:]

            if not cratemover_version == 9001:
                popped.reverse()

            heaps[move_from - 1] = heaps[move_from - 1][:-move_n]
            heaps[move_to - 1].extend(popped)

    print("".join([heap[-1] for heap in heaps]))


def part2():
    part1(9001)


if __name__ == "__main__":
    part1()
    part2()
