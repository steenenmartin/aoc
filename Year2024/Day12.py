
inpt = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

G = [[c for c in l] for l in inpt.split()]
R = len(G)
C = len(G[0])
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def explore_garden(v):
    r, c = v
    discovered.append(v)

    for i in range(len(d)):
        dr, dc = d[i]
        wr, wc = r + dr, c + dc

        if 0 <= wr < R and 0 <= wc < C and G[wr][wc] == G[r][c] and (wr, wc) not in discovered:
            explore_garden((wr, wc))

        elif (wr, wc) not in discovered:
            fences.append((wr, wc, i))


regions = []
p1 = 0
p2 = 0
for r in range(R):
    for c in range(C):
        v = (r, c)

        if any(region for region in regions if (r, c) in region):
            continue

        discovered = []
        fences = []
        explore_garden(v)
        regions.append(discovered)
        fences = sorted(fences)

        p1 += len(fences) * len(discovered)

        def get_side_fences(f):
            r, c, i = f
            side_fences.append(f)

            for dr, dc in d:
                wr, wc = r + dr, c + dc
                w = (wr, wc, i)

                if w in fences and w not in side_fences:
                    get_side_fences(w)

        sides = 0
        while fences:
            fence = fences.pop()
            side_fences = []
            get_side_fences(fence)
            for f in side_fences:
                if f in fences:
                    fences.remove(f)
            sides += 1

        p2 += sides * len(discovered)

print(p1)
print(p2)


