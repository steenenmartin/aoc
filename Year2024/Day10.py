from collections import defaultdict

inpt = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

G = [[int(c) for c in l] for l in inpt.split()]
R = len(G)
C = len(G[0])

zeros = []
for r in range(R):
    for c in range(C):
        if G[r][c] == 0:
            zeros.append((r, c, 0))


def dfs(v, exclude_discovered):
    r, c, h = v
    discovered.append(v)

    if h == 9:
        return 1

    res = 0
    for dr, dc in [(-1, 0), (1,0), (0, 1), (0, -1)]:
        rr, cc = r + dr, c + dc
        w = (rr, cc, h+1)
        if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == h + 1 and (exclude_discovered or w not in discovered):
            res += dfs(w, exclude_discovered)

    return res


for xclude_discovered in [False, True]:
    ans = 0
    for z in zeros:
        discovered = []
        ans += dfs(z, exclude_discovered=xclude_discovered)

    print(ans)
