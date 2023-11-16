import random


start_molecule = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"


def part1():
    rules = []
    for line in open("./Year2015/Input/input19.txt"):
        h, r = line.split(' => ')
        rules.append((h, r.strip()))
    new_molecules = set()
    for head, rep in rules:
        for i in range(len(start_molecule)):
            if start_molecule[i:i + len(head)] == head:
                m = start_molecule[:i] + rep + start_molecule[i + len(head):]
                new_molecules.add(m)
    print(len(new_molecules))


def part2():
    rules = []
    for line in open("./Year2015/Input/input19.txt"):
        h, r = line.split(' => ')
        rules.append((h, r.strip()))

    steps = 0
    mol = start_molecule[:]
    r = 0
    while r < len(rules):
        head, rep = rules[r]
        i = mol.find(rep)
        if i != -1:
            steps += 1
            mol = mol[:i] + head + mol[i + len(rep):]
            r = 0
            random.shuffle(rules)
            if mol == 'e':
                print(steps)
                return
        else:
            r += 1

