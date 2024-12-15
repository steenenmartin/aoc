
inpt = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
i_to_d = {"^": 0, ">": 1, "v": 2, "<": 3}
I = [i_to_d[i] for i in inpt.split("\n\n")[1]]
G = [["" if c == "." else c for c in l] for l in inpt.split("\n\n")[0].split("\n")]
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == "@":
            p = (r, c)
            G[r][c] = ""
            break

for i in I:
    dr, dc = ds[i]
    pr, pc = p
    if G[pr + dr][pc + dc] == "":
        p = pr + dr, pc + dc
        continue

    if G[pr + dr][pc + dc] == "#":
        continue

    j = 1
    while True:
        breaker = False
        jdr, jdc = dr * j, dc * j
        if G[pr + jdr][pc + jdc] == "":
            breaker = True
        elif G[pr + jdr][pc + jdc] == "#":
            j = 0
            breaker = True

        if breaker:
            break
        else:
            j += 1

    for j in range(j, 0, -1):
        jdr, jdc = dr * j, dc * j
        G[pr + jdr][pc + jdc] = G[pr + dr * (j-1)][pc + dc * (j-1)]
    if j > 0:
        p = pr + dr, pc + dc

p1 = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == "O":
            p1 += r * 100 + c

print(p1)

grid_lines = inpt.split("\n\n")[0].split("\n")
G = [[] for i in range(len(grid_lines))]
for i in range(len(grid_lines)):
    for c in grid_lines[i]:
        if c == "#":
            G[i].append(c)
            G[i].append(c)
        elif c == "O":
            G[i].append("[")
            G[i].append("]")
        elif c == ".":
            G[i].append(" ")
            G[i].append(" ")
        elif c == "@":
            G[i].append("@")
            G[i].append(" ")

R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == "@":
            p = (r, c)
            G[r][c] = " "
            break

for i in I:
    dr, dc = ds[i]
    pr, pc = p
    if G[pr + dr][pc + dc] == " ":
        p = pr + dr, pc + dc
        continue

    if G[pr + dr][pc + dc] == "#":
        continue

    # Horizontal, same logic as p1
    if i == 1 or i == 3:
        j = 1
        while True:
            breaker = False
            jdr, jdc = dr * j, dc * j
            if G[pr + jdr][pc + jdc] == " ":
                breaker = True
            elif G[pr + jdr][pc + jdc] == "#":
                j = 0
                breaker = True

            if breaker:
                break
            else:
                j += 1

        for j in range(j, 0, -1):
            jdr, jdc = dr * j, dc * j
            G[pr + jdr][pc + jdc] = G[pr + dr * (j-1)][pc + dc * (j-1)]
        if j > 0:
            p = pr + dr, pc + dc
    # Vertical, p2 specific logic
    else:
        move_ids = set([(pr, pc)])

        while True:
            if any(mid for mid in move_ids if G[mid[0] + dr][mid[1]] == "#"):
                move_ids = []
                break
            new_move_ids = []
            for move_id_r, move_id_c in move_ids:
                new_move_id_r, new_move_id_c = move_id_r + dr, move_id_c
                if G[new_move_id_r][new_move_id_c] == "[" or G[new_move_id_r][new_move_id_c] == "]":
                    new_move_ids.append((new_move_id_r, new_move_id_c))
                    if G[new_move_id_r][new_move_id_c] == "[":
                        new_move_ids.append((new_move_id_r, new_move_id_c + 1))
                    if G[new_move_id_r][new_move_id_c] == "]":
                        new_move_ids.append((new_move_id_r, new_move_id_c - 1))
            new_move_ids.append(p)
            new_move_ids = set(new_move_ids)
            if not any(new_move_ids.difference(move_ids)):
                break
            else:
                move_ids = move_ids.union(new_move_ids)

        move_ids = list(move_ids)
        move_ids.sort(reverse=i==2)
        moved = False
        while move_ids:
            moved = True
            move_id = move_ids.pop(0)

            if p == move_id:
                pass
            else:
                G[move_id[0] + dr][move_id[1]] = G[move_id[0]][move_id[1]]
                if G[move_id[0]][move_id[1]] != "#":
                    G[move_id[0]][move_id[1]] = " "
        if moved:
            p = pr + dr, pc + dc

p2 = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == "[":
            p2 += r * 100 + c

print(p2)

