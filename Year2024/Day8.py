import numpy as np

input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

m = np.matrix([[c for c in l] for l in input.split("\n")])
R, C = m.shape

antennas = {}
for r in range(m.shape[0]):
    for c in range(m.shape[1]):
        _m = m[r, c]
        if _m != ".":
            antennas[(r, c)] = _m

antenna_types = set(antennas.values())

found_antinodes = {}
for self_rc, self in antennas.items():
    for other_rc, other in antennas.items():
        if self_rc == other_rc:
            continue
        if self != other:
            continue
        if (self_rc, other_rc) in found_antinodes or (other_rc, self_rc) in found_antinodes:
            continue

        dr, dc = self_rc[0] - other_rc[0], self_rc[1] - other_rc[1]

        r1, c1 = self_rc[0] + dr, self_rc[1] + dc
        r2, c2 = other_rc[0] - dr, other_rc[1] - dc

        if 0 <= r1 < R and 0 <= c1 < C and not (r1, c1) in found_antinodes.values():
            found_antinodes[(self_rc, other_rc)] = (r1, c1)

        if 0 <= r2 < R and 0 <= c2 < C and not (r2, c2) in found_antinodes.values():
            found_antinodes[(other_rc, self_rc)] = (r2, c2)

print(len(found_antinodes))


found_antinodes = {}
for self_rc, self in antennas.items():
    for other_rc, other in antennas.items():
        if self_rc == other_rc:
            continue
        if self != other:
            continue
        if (self_rc, other_rc) in found_antinodes or (other_rc, self_rc) in found_antinodes:
            continue

        if not self_rc in found_antinodes.values():
            found_antinodes[(self_rc, other_rc, 0)] = self_rc
        if not other_rc in found_antinodes.values():
            found_antinodes[(other_rc, self_rc, 0)] = other_rc

        dr, dc = self_rc[0] - other_rc[0], self_rc[1] - other_rc[1]

        r1, c1 = self_rc[0] + dr, self_rc[1] + dc
        multiple = 0
        while 0 <= r1 < R and 0 <= c1 < C:
            if not (r1, c1) in found_antinodes.values():
                found_antinodes[(self_rc, other_rc, multiple)] = (r1, c1)
            r1, c1 = r1 + dr, c1 + dc
            multiple += 1

        r2, c2 = other_rc[0] - dr, other_rc[1] - dc
        multiple = -1
        while 0 <= r2 < R and 0 <= c2 < C:
            if not (r2, c2) in found_antinodes.values():
                found_antinodes[(other_rc, self_rc, multiple)] = (r2, c2)
            r2, c2 = r2 - dr, c2 - dc
            multiple -= 1


print(len(found_antinodes))
