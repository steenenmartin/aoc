import heapq
from collections import defaultdict

inpt = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

G = [[c for c in l] for l in inpt.split("\n")]
R = len(G)
C = len(G[0])

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


for r in range(R):
    for c in range(C):
        if G[r][c] == "#":
            continue

        if G[r][c] == "S":
            S = (r, c)
        if G[r][c] == "E":
            E = (r, c)
            G[r][c] = " "
        if G[r][c] == "":
            G[r][c] = " "

costs = {}
paths_to_node = defaultdict(list)


def dijkstra_pq(G, s):
    costs[(s, 1)] = 0
    pq = [(0, s, 1)]

    while pq:
        current_cost, current_node, current_direction = heapq.heappop(pq)

        if current_cost > costs[(current_node, current_direction)]:
            continue

        for new_direction in range(len(ds)):
            dr, dc = ds[new_direction]
            rr, cc = current_node[0] + dr, current_node[1] + dc
            turn = new_direction != current_direction
            cost = current_cost + turn * 1000 + 1
            new_node = (rr, cc)
            if G[rr][cc] != "#":
                if (new_node, new_direction) in costs:
                    if cost < costs[(new_node, new_direction)]:
                        costs[(new_node, new_direction)] = cost
                        heapq.heappush(pq, (cost, (rr, cc), new_direction))
                else:
                    heapq.heappush(pq, (cost, (rr, cc), new_direction))
                    costs[(new_node, new_direction)] = cost
                if cost <= costs.get((new_node, new_direction), -1):
                    paths_to_node[(new_node, new_direction)].extend([(current_node, current_direction)] + paths_to_node[(current_node, current_direction)])

            if new_node == E:
                paths_to_node[(new_node, new_direction)].append((new_node, new_direction))
                pq.clear()


dijkstra_pq(G, S)
print(costs[(E, 0)])

all_paths_to_E = set([vv[0] for n, v in paths_to_node.items() for vv in v if n[0] == E])
print(len(all_paths_to_E))
