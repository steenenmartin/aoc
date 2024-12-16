import heapq
from collections import defaultdict

inpt = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

G = [[c for c in l] for l in inpt.split("\n")]
R = len(G)
C = len(G[0])

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


distances = {}
for r in range(R):
    for c in range(C):
        if G[r][c] == "#":
            continue

        distances[(r, c)] = 1e100

        if G[r][c] == "S":
            S = (r, c)
        if G[r][c] == "E":
            E = (r, c)
            G[r][c] = " "
        if G[r][c] == "":
            G[r][c] = " "


def dijkstra_pq(G, s):
    distances[s] = 0
    pq = [(0, s, 1)]
    predecessors = defaultdict(list)

    while pq:
        current_dist, current_node, current_direction = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for i in range(len(ds)):
            dr, dc = ds[i]
            rr, cc = current_node[0] + dr, current_node[1] + dc

            if G[rr][cc] != "#":
                turn = i != current_direction
                distance = current_dist + turn * 1000 + 1

                if distance < distances[(rr, cc)]:
                    distances[(rr, cc)] = distance
                    heapq.heappush(pq, (distance, (rr, cc), i))
                    predecessors[(rr, cc)] = [current_node]

    return distances


def find_all_paths_with(start, end, cost):
    cache = {}

    def dfs(directed_node, current_cost):
        if current_cost > cost:
            return []

        node, direction = directed_node

        if node == end:
            if current_cost == cost:
                return [[end]]
            return []

        if (node, current_cost) in cache:
            return cache[(node, current_cost)]

        paths = []
        visited.add(node)
        for i in range(len(ds)):
            dr, dc = ds[i]
            rr, cc = node[0] + dr, node[1] + dc
            if (rr, cc) not in visited:
                if G[rr][cc] != "#":
                    turn = i != direction
                    c = current_cost + turn * 1000 + 1
                    subpaths = dfs(((rr, cc), i), c)
                    for subpath in subpaths:
                        paths.append([node] + subpath)
        visited.remove(node)

        cache[(node, current_cost)] = paths
        return paths

    visited = set()
    result = dfs((start, 1), 0)
    return result


cost_to_node = dijkstra_pq(G, S)
print(cost_to_node[E])

shortest_paths = find_all_paths_with(S, E, cost_to_node[E])

shortest_path_nodes = set()
for path in shortest_paths:
    shortest_path_nodes = shortest_path_nodes.union(path)

print(len(shortest_path_nodes))
