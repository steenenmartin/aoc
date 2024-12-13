
inpt = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def solve(add_10000000000000):
    res = 0
    for claw in inpt.split("\n\n"):
        for line in claw.split("\n"):
            line_split = line.split()
            if line_split[1] == "A:":
                xa = int(line_split[2].split("+")[1].strip(","))
                ya = int(line_split[3].split("+")[1])
            elif line_split[1] == "B:":
                xb = int(line_split[2].split("+")[1].strip(","))
                yb = int(line_split[3].split("+")[1])
            else:
                x = int(line_split[1].split("=")[1].strip(","))
                y = int(line_split[2].split("=")[1])

        if add_10000000000000:
            x += 10000000000000
            y += 10000000000000

        na = (x * yb - y * xb) / (xa * yb - xb * ya)
        nb = (x - na * xa) / xb

        if na % 1 == 0 and nb % 1 == 0:
            res += 3 * na + nb

    return int(res)


print(solve(False))
print(solve(True))
