import heapq
import itertools

from Year2021.Day11 import flash


def calculate_distances(graph, starting_vertex):
    distances = {vertex: 1e999 for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    discovering_edge = {}
    prev = None
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph[current_vertex]:
            distance = current_distance + 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                discovering_edge[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    paths = {v: [v] for v in graph.keys()}
    for end_vertex in discovering_edge.keys():
        vertex = end_vertex
        while vertex != starting_vertex:
            if discovering_edge[vertex] != starting_vertex:
                paths[end_vertex].append(discovering_edge[vertex])
            vertex = discovering_edge[vertex]

    return distances, paths


def part1():
    flow_rates = {}
    tunnels = {}
    with open("./Input/input16.txt") as f:
        for line in f.readlines():
            line = line.strip("\n")
            l1, l2 = line.split("to val")
            valve = l1.split(" ")[1]
            flow_rates[valve] = int(l1.split(" ")[4].strip("rate=").strip(";"))
            l2 = l2.replace(",", "")
            tunnels[valve] = l2.strip(",").split(" ")[1:]
    distances, paths = calculate_distances(tunnels, "AA")

    non_zero_valves = [k for k, v in flow_rates.items() if v != 0]
    permutations = [p for p in itertools.permutations(non_zero_valves, len(non_zero_valves))]

    current = "AA"
    for permutation in permutations:
        open_valves = {k: False for k in flow_rates.keys()}
        t = 0
        permutation = list(permutation)
        goal = permutation.pop()
        while t <= 30 and not all(v for v in open_valves.values()):
            t += 1
            if current == goal and not open_valves[current]:
                open_valves[current] = True
            else:
                distances, paths = calculate_distances(tunnels, current)
                if current == goal:
                    goal = permutation.pop()
                current = paths[goal].pop()



if __name__ == '__main__':
    part1()