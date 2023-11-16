import re

with open("./Input/input23.txt") as fp:
    input = fp.read()

instrs = [x for x in re.findall('^(\w+) (\S+)(?:, (\S+))?$', input, re.M)]


def day23(a, b):
    m = {
        'a': a,
        'b': b,
    }
    i = 0
    while 0 <= i < len(instrs):
        inst, r, f = instrs[i]
        if inst == 'hlf':
            m[r] //= 2
        elif inst == 'tpl':
            m[r] *= 3
        elif inst == 'inc':
            m[r] += 1
        elif inst == 'jmp':
            i += int(r) - 1
        elif inst == 'jie':
            if m[r] % 2 == 0:
                i += int(f) - 1
        elif inst == 'jio':
            if m[r] == 1:
                i += int(f) - 1
        i += 1
    return m


print(day23(0, 0))
print(day23(1, 0))