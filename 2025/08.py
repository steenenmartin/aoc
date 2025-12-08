
inpt = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

def d(p, q):
    return ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2 + (q[2] - p[2]) ** 2) ** 0.5

coords = [tuple(map(int, l.split(','))) for l in inpt.splitlines()]

dists = {}
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        p, q = coords[i], coords[j]
        dists[(p, q)] = d(p, q)

edges = sorted(dists.items(), key=lambda item: item[1])
circuits = []

print_top_3_circuit_len_connections = 11
for i, ((p, q), v) in enumerate(edges):
    if (i + 1) == print_top_3_circuit_len_connections:
        sorted_circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
        print(len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2]))

    if any(c for c in circuits if p in c and q in c):
        continue

    cp = [c for c in circuits if p in c]
    cq = [c for c in circuits if q in c]

    if cp:
        [cp] = cp
    if cq:
        [cq] = cq

    if cp and cq and cp != cq:
        # p og q har forskellige circuits. Merge.
        cp = cp.extend(cq)
        cq.clear()
    elif cp and not cq:
        # Kun p har circuit, tilføj q
        cp.append(q)
    elif cq and not cp:
        # Kun q har circuit, tilføj p
        cq.append(p)
    else:
        # Ingen circuit indeholder p eller q, nyt circuit
        circuits.append([p, q])

    if any(c for c in circuits if len(c) == len(coords)):
        print(p[0] * q[0])
        break
