import numpy as np

def part1():
    with open("./Input/input14.txt") as f:
        walls = set()
        for line in f.readlines():
            line = line.strip("\n")
            line = line.strip(" ")
            coords = [np.array((int(x.split(",")[0]), int(x.split(",")[1]))) for x in line.split(" -> ")]
            for i in range(len(coords) - 1):
                delta = coords[i+1] - coords[i]
                delta //= max(abs(delta))

                coord = coords[i]
                while not all(x == 0 for x in coord - coords[i+1]):
                    walls.add(tuple(coord))
                    coord += delta
                walls.add(tuple(coord))

        max_wall_depth = max(wall[1] for wall in walls)

        sands = set()

        def drop(sand):
            if sand[1] == max_wall_depth:
                return False

            blocked = walls.union(sands)
            while (sand[0], sand[1] + 1) not in blocked:
                sand = (sand[0], sand[1] + 1)

            if len({(sand[0]-1, sand[1] + 1), (sand[0], sand[1] + 1), (sand[0]+1, sand[1] + 1)}.intersection(blocked)) == 3:
                sands.add(sand)
                return True

            if (sand[0] - 1, sand[1] + 1) not in blocked:
                return drop((sand[0] - 1, sand[1] + 1))
            elif (sand[0] + 1, sand[1] + 1) not in blocked:
                return drop((sand[0] + 1, sand[1] + 1))

        while True:
            sand = (500, 0)
            abyss_drop = drop(sand)
            if abyss_drop is False:
                break

        print(len(sands))


def part2():
    with open("./Input/input14.txt") as f:
        q = set()
        t = 0
        for line in f.readlines():
            line = line.split(" -> ")
            for coord in range(len(line) - 1):
                a, b = line[coord], line[coord + 1]
                a, b = a.split(","), b.split(",")
                t = max(t, int(a[1]))
                t = max(t, int(b[1]))
                for xx in range(min(int(a[0]), int(b[0])), max(int(b[0]) + 1, int(a[0]) + 1)):
                    for yy in range(min(int(a[1]), int(b[1])), max(int(b[1]) + 1, int(a[1]) + 1)):
                        q.add((xx, yy))

        t += 1
        s = len(q)

        while True:
            a, b = 500, 0
            if (a, b) in q:
                print(len(q) - s)
                break

            while True:
                if b == t:
                    q.add((a, b))
                    break

                if (a, b + 1) not in q:
                    b += 1
                    continue
                else:
                    if (a - 1, b + 1) not in q:
                        a -= 1
                        b += 1
                        continue
                    elif (a + 1, b + 1) not in q:
                        a += 1
                        b += 1
                        continue

                q.add((a, b))
                break


if __name__ == "__main__":
    part1()
    part2()
