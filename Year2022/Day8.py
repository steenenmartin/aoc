import numpy as np


with open("./Input/input8.txt") as f:
    line_arrays = []
    for l in f.readlines():
        line_arrays.append([int(c) for c in l.strip("\n")])

    matrix = np.array(line_arrays)

visible = np.zeros_like(matrix)
visible[0, :], visible[:, 0], visible[-1, :], visible[:, -1] = [1] * 4  # Left, right upper and lower boundaries are visible

max_score = 0
for i in range(1, matrix.shape[0] - 1):
    for j in range(1, matrix.shape[1] - 1):
        # Trees to the left, right above and below the i, j tree
        tree_lines_ij = [
            matrix[i,:j][::-1],  # Reversed (increasing index is increasing distance from i, j) used for the distance-measuring in problem 2
            matrix[i, j + 1:],
            matrix[:i, j][::-1],  # Reversed (increasing index is increasing distance from i, j) used for the distance-measuring in problem 2
            matrix[i + 1:, j]
        ]

        if any(all(tree < matrix[i, j] for tree in tree_line) for tree_line in tree_lines_ij):
            # If all trees in any tree lines to the left, right above or below are lower than this tree, it is visible from outside
            visible[i, j] = 1

        distances = [len(t) for t in tree_lines_ij]
        for tree_line in range(len(tree_lines_ij)):
            # Looking through tree lines to the left, right, above or below

            for tree in range(len(tree_lines_ij[tree_line])):
                # Look at each tree in increasing distance from i, j

                if tree_lines_ij[tree_line][tree] >= matrix[i, j]:
                    # If tree is higher, distance is stored and the (inner) loop is breaked
                    distances[tree_line] = tree + 1  # distance is 1-indexed
                    break

        score = np.prod(distances)
        if score > max_score:
            max_score = score

print("p1", visible.sum())
print("p2", max_score)
