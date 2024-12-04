
input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def check_safe(rd):
    return all(-3 <= d < 0 for d in rd) or all(0 < d <= 3 for d in rd)


def calc_diff(report):
    return [report[i] - report[i-1] for i in range(1, len(report))]


def part1():
    reports = [[int(l) for l in r.split()] for r in input.split("\n")]

    s = 0
    for diffs in [calc_diff(r) for r in reports]:
        if check_safe(diffs):
            s += 1

    print(s)


def part2():
    reports = [[int(l) for l in r.split()] for r in input.split("\n")]
    report_diffs = [calc_diff(r) for r in reports]

    s = 0
    for i in range(len(report_diffs)):
        rd = report_diffs[i]
        if check_safe(rd):
            s += 1
        else:
            r = reports[i]
            for j in range(len(r)):
                r_updated = r[:j] + r[j+1:]
                updated_diffs = calc_diff(r_updated)
                if check_safe(updated_diffs):
                    s += 1
                    break

    print(s)


if __name__ == "__main__":
    part1()
    part2()
