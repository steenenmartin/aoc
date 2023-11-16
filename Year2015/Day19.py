import math
import re
from itertools import combinations

import pandas as pd
import numpy as np


def part1():
    replacements = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg"""

    replacement_list = []
    for s in replacements.split("\n"):
        replacement_list.append((s.split(" ")[0], s.split(" ")[2]))

    input_str = ""

    molecule = input_str.split('\n')[-1][::-1]
    reps = {m[1][::-1]: m[0][::-1] for m in re.findall(r'(\w+) => (\w+)', input_str)}

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

