
raw_inpt = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

inpt = [l.split() for l in raw_inpt.splitlines()]
R = len(inpt)
C = len(inpt[0])

p1 = 0
for c in range(C):
    add = inpt[R - 1][c] == "+"
    mul = inpt[R - 1][c] == "*"
    res = 1 if mul else 0
    for r in range(R - 1):
        if add:
            res += int(inpt[r][c])
        if mul:
            res *= int(inpt[r][c])
    p1 += res

print(p1)

inpt_lines = raw_inpt.splitlines()
splits = []
for i in range(len(inpt_lines[0])):
    if all(l[i] == " " for l in inpt_lines):
        splits.append(i)
splits.append(len(inpt_lines[0]))

p2 = 0
last_split = 0
n_split = 0
for split in splits:
    add = inpt[R - 1][n_split] == "+"
    mul = inpt[R - 1][n_split] == "*"
    res = 1 if mul else 0
    for c in range(last_split, split):
        col = ""
        for r in range(R - 1):
            if inpt_lines[r][c] != " ":
                col += inpt_lines[r][c]

        if add:
            res += int(col)
        if mul:
            res *= int(col)
    p2 += res
    last_split = split + 1
    n_split += 1
print(p2)
