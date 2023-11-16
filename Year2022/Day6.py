

def part12(j):
    with open("./Input/input6.txt") as f:
        for line in f.readlines():
            for i in range(j, len(line)):
                if len(set(line[i-j:i])) == j:
                    print(i)
                    break


if __name__ == "__main__":
    part12(4)
    part12(14)
