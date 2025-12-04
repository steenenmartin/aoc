
inpt = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

grid = [[c == "@" for c in r] for r in inpt.split("\n")]
R, C  = len(grid), len(grid[0])
deltas = ((-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1), (1, 0), (0, -1), (0, 1))


def solve(do_removals: bool):
    ans = 0
    removed = True
    while removed:
        removed = False
        for r in range(R):
            for c in range(C):
                if not grid[r][c]:
                    continue
                    
                n = 0
                for dr, dc in deltas:
                    if n >= 4:
                        break

                    if 0 <= r + dr < R and 0 <= c + dc < C:
                        if grid[r + dr][c + dc]:
                            n += 1

                if n < 4:
                    ans += 1
                    if do_removals:
                        grid[r][c] = False
                        removed = True

    return ans


print(solve(False))
print(solve(True))
