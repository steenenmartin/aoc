import numpy as np

inpt = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

ps = []
vs = []
for l in inpt.split("\n"):
    l_split = l.split()
    ps.append([int(l_split[0].split("=")[1].split(",")[1]), int(l_split[0].split("=")[1].split(",")[0])])
    vs.append([int(l_split[1].split("=")[1].split(",")[1]), int(l_split[1].split("=")[1].split(",")[0])])


p = np.matrix(ps)
v = np.matrix(vs)

test_input = len(ps) == 12 
R = 7 if test_input else 103
C = 11 if test_input else 101

Rm = R // 2
Cm = C // 2

m = np.zeros((R, C))

pic = []
s = 0
while True:
    p = p + v
    p += np.where(p < 0, 1, 0) * np.array([R, C])
    p = np.remainder(p, [R, C])
    m *= 0
    for _p in p:
        m[_p[0, 0], _p[0, 1]] = 1

    if not test_input:
        pic = []
        pic.append("================================================================================================")
        pic.append(str(s))
        candidate = False
        for r in range(R):
            pic_line = ""
            for c in range(C):
                pic_line += " " if m[r, c] == 0 else "#"
            if "###############################" in pic_line:
                candidate = True
            pic.append(pic_line)
        pic.append("================================================================================================")
        if candidate:
            for pp in pic:
                print(pp)
            break

    if s == 99:
        q1, q2, q3, q4 = 0, 0, 0, 0
        for _p in p:
            r, c = _p[0, 0], _p[0, 1]
            if r < Rm and c < Cm:
                q1 += 1
            elif r < Rm and c > Cm:
                q2 += 1
            elif r > Rm and c > Cm:
                q3 += 1
            elif r > Rm and c < Cm:
                q4 += 1

        print(q1 * q2 * q3 * q4)
        if test_input:
            break

    s += 1




