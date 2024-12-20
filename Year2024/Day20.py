
inpt = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


G = [[c for c in l] for l in inpt.split("\n")]

R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == "S":
            S = (r, c)
        elif G[r][c] == "E":
            E = (r, c)

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d2s = [(-2, 0), (0, 2), (2, 0), (0, -2)]


current = S

dist_to_end = {S: 0}
while current != E:
    r, c = current
    for dr, dc in ds:
        pr, pc = r + dr, c + dc
        if G[pr][pc] != "#" and (pr, pc) not in dist_to_end:
            dist_to_end = {k: v+1 for k, v in dist_to_end.items()}
            current = (pr, pc)
            dist_to_end[current] = 0
            break

distance_saving_cheats = 0
for p1 in dist_to_end:
    for p2 in [p for p in dist_to_end if dist_to_end[p] < dist_to_end[p1] and (p[0] - p1[0], p[1]-p1[1]) in d2s]:
        delta = dist_to_end[p1] - dist_to_end[p2] - 2
        if delta >= 100:
            distance_saving_cheats += 1
print(distance_saving_cheats)

distance_saving_cheats = 0
for p1 in dist_to_end:
    for p2 in [p for p in dist_to_end if dist_to_end[p] < dist_to_end[p1] and abs(p[0] - p1[0]) + abs(p[1]-p1[1]) <= 20]:
        dist = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
        delta = dist_to_end[p1] - dist_to_end[p2] - dist
        if delta >= 100:
            distance_saving_cheats += 1
print(distance_saving_cheats)

