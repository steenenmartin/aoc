
inpt = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

connections = {}
for line in inpt.splitlines():
    l = line.replace(":", "").split()
    connections[l[0]] = l[1:]

cache = {}
def dfs(start, end):
    if (start, end) in cache:
        return cache[(start, end)]

    if start == end:
        cache[(start, end)] = 1
        return 1

    if start not in connections:
        return 0

    cache[(start, end)] = sum(dfs(v, end) for v in connections[start])
    return cache[(start, end)]


print(dfs("you", "out"))

print(
    dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out")
    + dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")
)
