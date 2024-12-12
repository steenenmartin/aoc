
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


# Recursively explore garden which contains a plant 'p'
def explore_garden(p):
    r, c = p
    discovered.append(p)

    for i in range(len(d)):
        dr, dc = d[i]
        pr, pc = r + dr, c + dc

        if 0 <= pr < R and 0 <= pc < C and G[pr][pc] == G[r][c] and (pr, pc) not in discovered:
            explore_garden((pr, pc))

        elif (pr, pc) not in discovered:
            # If pr, pc is not added to this garden, it is considered a fence.
            # The direction 'i' we were looking in is stored as well in order to enable identification entire fence sides in part 2
            fences.append((pr, pc, i))


gardens = []
p1 = 0
p2 = 0

# Loop through all plants
for r in range(R):
    for c in range(C):
        plant = (r, c)

        # If garden is already explored, continue
        if any(garden for garden in gardens if (r, c) in garden):
            continue

        discovered = []
        fences = []
        explore_garden(plant)

        # Store discovered plants as a garden in order for the continue above to work
        gardens.append(discovered)

        p1 += len(fences) * len(discovered)

        # Recursively explore same side fences to a fence 'f'
        def same_side_fences(f):
            r, c, i = f
            side_fences.append(f)

            for dr, dc in d:
                fr, fc = r + dr, c + dc
                w = (fr, fc, i)

                if w in fences and w not in side_fences:
                    same_side_fences(w)

        sides = 0
        while fences:
            # Pops a fence, removes same side fences and count sides one up
            fence = fences.pop()
            side_fences = []
            same_side_fences(fence)
            for f in side_fences:
                if f in fences:
                    fences.remove(f)
            sides += 1

        p2 += sides * len(discovered)

print(p1)
print(p2)
