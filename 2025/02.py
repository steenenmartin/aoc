inpt = """959516-995437,389276443-389465477,683-1336,15687-26722,91613-136893,4-18,6736-12582,92850684-93066214,65-101,6868676926-6868700146,535033-570760,826141-957696,365650-534331,1502-2812,309789-352254,79110404-79172400,18286593-18485520,34376-65398,26-63,3333208697-3333457635,202007-307147,1859689-1936942,9959142-10053234,2318919-2420944,5142771457-5142940464,1036065-1206184,46314118-46413048,3367-6093,237-481,591751-793578"""

id_pairs = [(s.split("-")[0], s.split("-")[1]) for s in inpt.split(",")]

p1 = 0
for id1, id2 in id_pairs:
    for i in range(int(id1), int(id2)+2):
        i_string = str(i)
        if len(i_string) % 2 != 0:
            continue

        i0 = i_string[:len(i_string) // 2]
        i1 = i_string[len(i_string) // 2:]

        if i0 == i1:
            p1 += i

print(p1)

p2 = 0
for id1, id2 in id_pairs:
    for i in range(int(id1), int(id2)+2):
        i_string = str(i)
        for n in range(1, len(str(i))):
            if len(i_string) % n != 0:
                continue

            x = len(i_string) // n

            substrs = set()
            for _x in range(x):
                substrs.add(i_string[n*_x:n*_x+n])

            if len(substrs) == 1:
                print(i)
                p2 += i
                break

print(p2)
