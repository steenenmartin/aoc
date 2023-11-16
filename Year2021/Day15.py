import heapq
import math
from collections import defaultdict

import numpy as np


def part1():
    with open("Input/input15.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    risk_matrix = np.zeros((len(input), len(input[0])))
    for i in range(risk_matrix.shape[0]):
        for j in range(risk_matrix.shape[1]):
            risk_matrix[i, j] = input[i][j]

    total_risk_matrix = np.zeros_like(risk_matrix) + 1e10
    total_risk_matrix[0, 0] = 0

    dijkstra(risk_matrix, total_risk_matrix)

    print(total_risk_matrix[-1, -1])


def part2():
    with open("Input/input15.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    n = len(input)
    m = len(input[0])
    risk_matrix = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            risk_matrix[i, j] = input[i][j]

    full_risk_matrix = np.zeros((n*5, m*5))
    for i in range(5):
        for j in range(5):
            full_risk_matrix[i*n:i*n+n, j*m:j*m+m] = np.mod(risk_matrix + (i + j), 9)
    full_risk_matrix += np.where(full_risk_matrix == 0, 9, 0)
    shortest_risk_matrix = np.zeros_like(full_risk_matrix) + 1e10
    shortest_risk_matrix[0, 0] = 0

    dijkstra(full_risk_matrix, shortest_risk_matrix)

    print(shortest_risk_matrix[-1, -1])


def part2_2():
    with open("Input/input15.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    n = len(input)
    m = len(input[0])
    risk_matrix = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            risk_matrix[i, j] = input[i][j]

    full_risk_matrix = np.zeros((n*5, m*5))
    for i in range(5):
        for j in range(5):
            full_risk_matrix[i*n:i*n+n, j*m:j*m+m] = np.mod(risk_matrix + (i + j), 9)
    full_risk_matrix += np.where(full_risk_matrix == 0, 9, 0)

    shortest_risk = dijkstra_pq(full_risk_matrix, (0, 0), (full_risk_matrix.shape[0] - 1, full_risk_matrix.shape[1] - 1))

    print(shortest_risk)


def dijkstra_pq(risk_matrix, start, end):
    shortest_risk = defaultdict(lambda: math.inf)
    shortest_risk[(start[0], start[1])] = 0
    visited = defaultdict(lambda: False)
    visited[(0, 0)] = True
    Q = [(0, (0, 0))]
    heapq.heapify(Q)

    while Q:
        risk, u = heapq.heappop(Q)

        if risk <= shortest_risk[u[0], u[1]]:
            for v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                p = (u[0] + v[0], u[1] + v[1])

                if not (0 <= p[0] < risk_matrix.shape[0] and 0 <= p[1] < risk_matrix.shape[1]):
                    continue

                new_risk = risk_matrix[p] + risk

                if p not in shortest_risk or new_risk < shortest_risk[p]:
                    shortest_risk[p] = new_risk
                    heapq.heappush(Q, (new_risk, p))

    return shortest_risk[end]


def dijkstra(risk_matrix, shortest_risk_matrix):
    removed = np.zeros_like(shortest_risk_matrix)
    while not np.all(removed):
        print(np.sum(1-np.where(removed != 0, 1, 0)))
        x, y = np.unravel_index(np.argmin(shortest_risk_matrix + removed), shortest_risk_matrix.shape)
        removed[x, y] += 1e10

        for move in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            try_set_dist(shortest_risk_matrix, risk_matrix, x, y, move[0], move[1])


def try_set_dist(shortest_risk_matrix, risk_matrix, x, y, i, j):
    if not (0 <= x + i < risk_matrix.shape[0] and 0 <= y + j < risk_matrix.shape[1]):
        return

    new_dist = shortest_risk_matrix[x, y] + risk_matrix[x + i, y + j]

    if new_dist < shortest_risk_matrix[x + i, y + j]:
        shortest_risk_matrix[x + i, y + j] = new_dist
