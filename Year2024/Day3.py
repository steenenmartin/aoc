
input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def solve(enable_disable):
    i = 0
    s = 0
    enabled = True
    while i < len(input):
        if input[i:i+4] == "do()":
            enabled = True
            i += 3
        if input[i:i+7] == "don't()":
            enabled = False
            i += 6
        if input[i:i + 4] == "mul(":
            i += 3
            m1, m2 = "", ""
            sep = False
            while True:
                i += 1
                if input[i].isdigit():
                    if sep:
                        m2 += input[i]
                    else:
                        m1 += input[i]
                elif input[i] == ",":
                    sep = True
                    continue
                elif input[i] == ")":
                    if enabled or not enable_disable:
                        s += int(m1) * int(m2)
                    break
                else:
                    break
        i += 1

    print(s)


if __name__ == "__main__":
    solve(False)
    solve(True)
