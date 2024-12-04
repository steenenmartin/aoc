import numpy as np

input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


matrix = np.matrix([[c for c in l] for l in input.split("\n")])

search_directions = [
    (0,   1),
    (1,   0),
    (0,  -1),
    (-1,  0),
    (1,   1),
    (-1,  1),
    (-1, -1),
    (1,  -1),
]

s = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        for ii, jj in search_directions:
            if 0 <= i + ii * 3 < matrix.shape[0] and 0 <= j + jj * 3 < matrix.shape[1]:
                chars = ""
                for x in range(4):
                    chars += matrix[int(i + x * ii), int(j + x * jj)]
                if chars == "XMAS":
                    s += 1
print(s)

s = 0
for i in range(1, matrix.shape[0] - 1):
    for j in range(1, matrix.shape[1] - 1):
        if matrix[i, j] == "A":
            if (matrix[i - 1, j - 1] == "M" and matrix[i + 1, j + 1] == "S") or (matrix[i - 1, j - 1] == "S" and matrix[i + 1, j + 1] == "M"):
                if (matrix[i - 1, j + 1] == "M" and matrix[i + 1, j - 1] == "S") or (matrix[i - 1, j + 1] == "S" and matrix[i + 1, j - 1] == "M"):
                    s += 1
print(s)

