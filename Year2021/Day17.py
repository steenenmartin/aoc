

def part1():
    x1 = 241
    x2 = 275

    y1 = -49
    y2 = -75

    max_ys = []
    for vx in range(30, 100):
        for vy in range(1000):
            x0 = y0 = 0
            maxy = 0
            while x0 <= x2 and y0 >= y2:
                x0 += vx
                y0 += vy

                if y0 > maxy:
                    maxy = y0

                if x1 <= x0 <= x2 and y1 >= y0 >= y2:
                    max_ys.append(maxy)
                    break

                if vx > 0:
                    vx -= 1

                vy -= 1

    print(max(max_ys))
