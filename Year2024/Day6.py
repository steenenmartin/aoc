import numpy as np

input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

m = np.matrix([[c for c in l] for l in input.split("\n")])
R, C = m.shape
start_value = np.where(m == "^")
starting_position_rc = (start_value[0][0], start_value[1][0]) if start_value[0].size > 0 else None
position_rc = starting_position_rc
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

d = 0
dr, dc = ds[0]
while True:
    m[position_rc] = "X"
    r, c = position_rc

    if r + dr == -1 or r + dr == R or c + dc == -1 or c + dc == C:
        break

    if m[r + dr, c + dc] != "#":
        position_rc = r + dr, c + dc
    else:
        d = (d + 1) % 4
        dr, dc = ds[d]
        position_rc = r + dr, c + dc

xs = [[x[0], x[1]] for x in np.argwhere(m == "X")]

print(len(xs))

m = np.matrix([[c for c in l] for l in input.split("\n")])

ps = 0
for obstacle in xs:
    obst_r, obst_c = obstacle
    if m[obst_r, obst_c] == "#" or obstacle == starting_position_rc:
        continue

    pos_dir_cache = set()
    r, c = starting_position_rc
    d = 0
    dr, dc = ds[d]

    while True:
        pos_dir = (r, c, d)
        if pos_dir in pos_dir_cache:
            ps += 1
            break
        else:
            pos_dir_cache.add(pos_dir)

        if r + dr < 0 or r + dr == R or c + dc == -1 or c + dc == C:
            break

        while m[r + dr, c + dc] == "#" or (r + dr == obst_r and c + dc == obst_c):
            d = (d + 1) % 4
            dr, dc = ds[d]

        r, c = r + dr, c + dc

print(ps)
