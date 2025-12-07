inpt = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

grid = [[c for c in l] for l in inpt.splitlines()]
R = len(grid)
C = len(grid[0])

beams = []
for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            start = (r,c)
            break

beams.append(start)
splits = 0
while not all(r == R for (r, c) in beams):
    r, c = beams.pop(0)
    if r == R - 1 :
        continue

    r += 1
    if grid[r][c] == "^":
        if not (r, c - 1) in beams:
            beams.append((r, c - 1))
        if not (r, c + 1) in beams:
            beams.append((r, c + 1))
        splits += 1
    else:
        if not (r, c) in beams:
            beams.append((r, c))
print(splits)

cache = {}
paths = 0
def solve(starting_point):
    if starting_point in cache:
        return cache[starting_point]

    r, c = starting_point
    while grid[r][c] != "^":
        r += 1
        if r == R - 1:
            cache[starting_point] = 1
            return 1

    cache[starting_point] = solve((r, c - 1)) + solve((r, c + 1))
    return cache[starting_point]

print(solve(start))
