import numpy as np
import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: 1e999 for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


with open("input.txt") as f:
    heights = []
    for line in f.readlines():
        line = line.strip("\n")
        line_heights = [c for c in line]
        heights.append(line_heights)

    heights_matrix = np.matrix(heights)
    (start_x, start_y) = np.where(heights_matrix == 'S')[0][0], np.where(heights_matrix == 'S')[1][0]
    (end_x, end_y) = np.where(heights_matrix == 'E')[0][0], np.where(heights_matrix == 'E')[1][0]
    heights_matrix[heights_matrix == "S"] = "a"
    heights_matrix[heights_matrix == "E"] = "z"

    height_map = lambda c: ord(c) - 97
    heights_matrix = np.vectorize(height_map)(heights_matrix)

    graph = {}
    for i in range(heights_matrix.shape[0]):
        for j in range(heights_matrix.shape[1]):
            graph[(i, j)] = {}
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i + direction[0] < heights_matrix.shape[0] and 0 <= j + direction[1] < heights_matrix.shape[1]:
                    if heights_matrix[i + direction[0], j + direction[1]] <= heights_matrix[i, j] + 1:
                        graph[(i, j)][(i + direction[0], j + direction[1])] = 1

    possible_starting_points = [(np.where(heights_matrix == 0)[0][x], np.where(heights_matrix == 0)[1][x]) for x in range(len(np.where(heights_matrix == 0)[0]))]
    min_dist = 1e999
    for starting_point in possible_starting_points:
        dist = calculate_distances(graph, starting_point)[(end_x, end_y)]
        if dist < min_dist:
            min_dist = dist

    print(min_dist)
