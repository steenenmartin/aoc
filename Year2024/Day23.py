import itertools
from collections import defaultdict

inpt = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

cons = [(l.split("-")[0], l.split("-")[1]) for l in inpt.split("\n")]

g = defaultdict(list)

for c in cons:
    g[c[0]].append(c[1])
    g[c[1]].append(c[0])

cliques = list()


def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        if len(R) >= 3:
            cliques.append(R)
            return
    for v in list(P):
        bron_kerbosch(R.union({v}),
                      P.intersection(graph[v]),
                      X.intersection(graph[v]),
                      graph)
        P.remove(v)
        X.add(v)


nodes = set(g.keys())
bron_kerbosch(set(), nodes, set(), g)


cliques_3 = set()
for c in cliques:
    if len(c) > 3:
        for x in itertools.permutations(c, 3):
            cliques_3.add(tuple(sorted(x)))
    else:
        cliques_3.add(tuple(c))

print(sum(any(cc.startswith("t") for cc in c) for c in cliques_3))
print(",".join(list(sorted([c for c in [c for c in cliques if len(c) == max(len(c) for c in cliques)][0]]))))
