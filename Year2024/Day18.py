import heapq

inpt = """"""


bytes = [(int(l.split(",")[1]), int(l.split(",")[0])) for l in inpt.split("\n")]
R = 71
C = 71
G = []

for r in range(R):
    G.append([])
    for c in range(C):
        G[r].append("")

for i in range(1024):
    r, c = bytes[i]
    G[r][c] = "#"

S = (0, 0)
E = (R-1, C-1)
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

costs = {}
def dijkstra_pq(G, s):
    costs[s] = 0
    pq = [(0, s)]

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_cost > costs[current_node]:
            continue

        for new_direction in range(len(ds)):
            dr, dc = ds[new_direction]
            rr, cc = current_node[0] + dr, current_node[1] + dc
            cost = current_cost + 1
            new_node = (rr, cc)
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != "#":
                if cost < costs.get(new_node, 1e100):
                    costs[new_node] = cost
                    heapq.heappush(pq, (cost, (rr, cc)))

dijkstra_pq(G, S)
print(costs[E])

i += 1
while True:
    byte_r, byte_c = bytes[i]
    G[byte_r][byte_c] = "#"
    costs = {}
    dijkstra_pq(G, S)

    if not E in costs:
        print(f"{byte_c},{byte_r}")
        break

    i += 1
