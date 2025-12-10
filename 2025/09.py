
inpt = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

red_tiles = [tuple(map(int, v.split(","))) for v in inpt.split()]
red_tiles_for_edges = red_tiles.copy()
red_tiles_for_edges.append(red_tiles[0])

x_max, y_max = max(r[0] for r in red_tiles), max(r[1] for r in red_tiles)

areas = {}
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        (y0, x0), (y1, x1) = red_tiles[i], red_tiles[j]
        area = (abs(y1 - y0) + 1) * (abs(x1 - x0) + 1)
        areas[((y0, x0), (y1, x1))] = area

sorted_areas = sorted(areas.items(), key=lambda x: x[1], reverse=True)
print(sorted_areas[0][1])

def point_in_rect(p, q, r):
    (x0, y0), (x1, y1) = p, q
    xr, yr = r
    return (min(x0, x1) < xr < max(x0, x1) and min(y0, y1) < yr < max(y0, y1))

edges = []
for i in range(len(red_tiles_for_edges) - 1):
    t1, t2 = red_tiles_for_edges[i], red_tiles_for_edges[i + 1]
    dx, dy = t2[0] - t1[0], t2[1]- t1[1]
    direction = (0 if not dx else dx // abs(dx), 0 if not dy else dy // abs(dy))
    p = t1
    while p != t2:
        edges.append(p)
        p = p[0] + direction[0], p[1] + direction[1]

for (p, q), a in sorted_areas:
    if any(point_in_rect(p, q, r) for r in red_tiles):
        continue

    if not any(point_in_rect(p, q, r) for r in edges):
        print(a)
        break
