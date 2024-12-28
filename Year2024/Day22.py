from collections import defaultdict

inpt = """1
2
3
2024"""


def mix(n, by):
    return n ^ by


def prune(n):
    return n % 16777216


xs = [int(x) for x in inpt.split("\n")]


p1 = 0
changes = set()
change_count = defaultdict(int)
ii = 0
max_change_i_for_change = defaultdict(dict)
for x in xs:
    change = []
    for i in range(2000):
        x0 = x % 10
        res = x * 64
        x = mix(res, x)
        x = prune(x)

        res = x // 32
        x = mix(res, x)
        x = prune(x)

        res = x * 2048
        x = mix(res, x)
        x = prune(x)
        x1 = x % 10
        ch = x1 - x0
        change_tuple = tuple(change)

        if len(change) == 4:
            changes.add(change_tuple)
            change_count[change_tuple] += 1
            change.pop(0)
        change.append(ch)

        if change_tuple not in max_change_i_for_change[ii]:
            max_change_i_for_change[ii][change_tuple] = x0

    p1 += x
    ii += 1
print(p1)


p2 = 0
for chng in set(sorted(changes, key=lambda x: change_count[x], reverse=True)):
    s = 0
    for i in max_change_i_for_change:
        if chng in max_change_i_for_change[i]:
            s += max_change_i_for_change[i][chng]

    if s > p2:
        p2 = s

print(p2)
