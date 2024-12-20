patterns = "r, wr, b, g, bwu, rb, gb, br".split(", ")

designs = """brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".split("\n")


def check_arrangements(design):
    if len(design) == 0:
        return 1

    if design in cache:
        return cache[design]

    arrangements = 0
    for i in range(1, len(design) + 1):
        left = design[:i]
        right = design[i:]

        if left in patterns:
            arrangements += check_arrangements(right)

    cache[design] = arrangements
    return arrangements


cache = {}
print(sum(check_arrangements(design) > 0 for design in designs))
print(sum(map(check_arrangements, designs)))
