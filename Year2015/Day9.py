import itertools
import numpy as np


def part1():
    with open("./Year2015/Input/input9.txt") as fp:
        input = [x.strip("\n").split(" ") for x in fp.readlines()]

    nodes = set(x[0] for x in input).union(set(x[2] for x in input))
    node_dict = {}
    i = 0
    for node in nodes:
        node_dict[node] = i
        i += 1

    cost = {}
    for node in input:
        cost[(node[0], node[2])] = int(node[-1])
        cost[(node[2], node[0])] = int(node[-1])

    cost_matrix = np.zeros((len(nodes), len(nodes)))
    for node_i in nodes:
        for node_j in nodes:
            if (node_i, node_j) in cost:
                cost_matrix[node_dict[node_i], node_dict[node_j]] = cost[node_i, node_j]
                cost_matrix[node_dict[node_j], node_dict[node_i]] = cost[node_j, node_i]

    map = list(itertools.permutations(nodes))

    route_lenghts = []
    for i in range(len(map)):
        sum = 0
        route = map[i]
        prev = None
        for node in route:
            if prev is None:
                prev = node
                continue

            sum += cost[(prev, node)]

            prev = node

        route_lenghts.append(sum)

    print(max(route_lenghts))






