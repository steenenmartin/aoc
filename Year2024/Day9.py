
inpt = "2333133121414131402"


def generate_file_system(max_len_one):
    space = False
    file_system = []
    pos = 0
    id = 0
    for c in inpt:
        v = int(c)
        if max_len_one:
            for i in range(v):
                file_system.append((pos, 1, id if not space else -1))
                pos += 1
        else:
            file_system.append((pos, v, id if not space else -1))
            pos += v
        if space:
            id += 1
        space = not space
    return file_system


def checksum(file_system):
    for i in range(len(file_system)):
        f = file_system[-(i+1)]
        if f[2] != -1:
            for j in range(len(file_system)):
                s = file_system[j]
                if s[0] > f[0]:
                    continue
                if s[1] < f[1]:
                    continue
                if s[2] == -1:
                    if s[1] == f[1]:
                        file_system[j] = (s[0], f[1], f[2])
                        file_system[-(i+1)] = (f[0], s[1], s[2])
                        break
                    else:
                        d = s[1] - f[1]
                        file_system[j] = (s[0], f[1], f[2])
                        file_system.insert(j+1, (s[0] + f[1], d, -1))
                        file_system[-(i+1)] = (f[0], f[1], -1)
                        break
    s = 0
    for f in file_system:
        if f[2] == -1:
            continue
        for i in range(f[1]):
            s += (f[0] + i) * f[2]

    return s


print(checksum(generate_file_system(True)))
print(checksum(generate_file_system(False)))

