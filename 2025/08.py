
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

edges = sorted(dists.items(), key=lambda p: p[1])

circuits = []
point_to_circuit = {}
i = 0
print_top_3_circuit_len_connections = 11

for (p, q), dist in edges:
    cp = point_to_circuit.get(p)
    cq = point_to_circuit.get(q)

    i += 1
    if i == print_top_3_circuit_len_connections:
        sorted_circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
        print(len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2]))

    if cp is None and cq is None:
        # Ingen circuit indeholder p eller q, nyt circuit
        idx = len(circuits)
        circuits.append([p, q])
        point_to_circuit[p] = point_to_circuit[q] = idx

    elif cp is not None and cq is None:
        # Kun p har circuit, tilføj q
        circuits[cp].append(q)
        point_to_circuit[q] = cp

    elif cp is None and cq is not None:
        # Kun q har circuit, tilføj p
        circuits[cq].append(p)
        point_to_circuit[p] = cq

    elif cp != cq:
        # p og q har forskellige circuits. Merge.
        a, b = sorted([cp, cq])
        circuits[a].extend(circuits[b])
        for r in circuits[b]:
            point_to_circuit[r] = a
        circuits[b] = []

    if any(c for c in circuits if len(c) == len(coords)):
        print(p[0] * q[0])
        break
