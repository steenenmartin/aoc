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
while not all(b[0] == R for b in beams):
    beam = beams.pop(0)
    if beam[0] == R - 1 :
        continue
    new_beam = (beam[0] + 1, beam[1])
    if grid[new_beam[0]][new_beam[1]] == "^":
        if not (new_beam[0], new_beam[1] - 1) in beams:
            beams.append((new_beam[0], new_beam[1] - 1))
        if not (new_beam[0], new_beam[1] + 1) in beams:
            beams.append((new_beam[0], new_beam[1] + 1))
        splits += 1
    else:
        if not new_beam in beams:
            beams.append(new_beam)
print(splits)

cache = {}
paths = 0
def solve(starting_point):
    if starting_point in cache:
        return cache[starting_point]
    
    p = starting_point
    while grid[p[0]][p[1]] != "^":
        p = (p[0] + 1, p[1])
        if p[0] == R - 1:
            cache[starting_point] = 1
            return 1

    left = solve((p[0], p[1] - 1))
    right = solve((p[0], p[1] + 1))
    cache[starting_point] = left + right
    return left + right 

print(solve(start))
