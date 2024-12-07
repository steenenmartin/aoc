
input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

equations = [(int(l.split(":")[0]), [int(ll) for ll in l.split(":")[1].split()]) for l in input.split("\n")]


def backtrack(idx, cur_res, use_concat=False):
    if idx == len(numbers):
        if cur_res == target:
            res.append(cur_res)
        return
    backtrack(idx + 1, cur_res + numbers[idx], use_concat)
    backtrack(idx + 1, cur_res * numbers[idx], use_concat)

    if use_concat:
        backtrack(idx + 1, int(str(cur_res) + str(numbers[idx])), use_concat)


for use_concat in [False, True]:
    s = 0
    for target, numbers in equations:
        n = len(numbers)
        res = []
        backtrack(1, numbers[0], use_concat)
        if res:
            s += res[0]

    print(s)
