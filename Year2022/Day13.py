import json


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return None
    elif isinstance(left, list) and isinstance(right, list):
        left = list(reversed(left))
        right = list(reversed(right))

        while len(right) > 0 or len(left) > 0:
            if len(left) == 0 and len(right) > 0:
                return True
            elif len(left) > 0 and len(right) == 0:
                return False
            else:
                ll = left.pop()
                rr = right.pop()
                res = compare(ll, rr)
                if res is not None:
                    return res
    elif isinstance(left, list) and isinstance(right, int):
        right = [right]
        return compare(left, right)
    elif isinstance(right, list) and isinstance(left, int):
        left = [left]
        return compare(left, right)
    else:
        raise NotImplementedError


with open("input.txt") as f:
    lines = []
    for line in f.readlines():
        line = line.strip("\n")

        if line == "":
            continue

        lines.append(json.loads(line))

    lefts = lines[::2]
    rights = lines[1::2]

    assert len(lefts) == len(rights)

    ordered = []
    for i in range(len(lefts)):
        if compare(lefts[i], rights[i]):
            ordered.append(i + 1)
    print(sum(ordered))

with open("input.txt") as f:
    lines = []
    for line in f.readlines():
        line = line.strip("\n")

        if line == "":
            continue

        lines.append(json.loads(line))

    lines.append([[2]])
    lines.append([[6]])

    lines = list(reversed(lines))
    sorted_packets = [lines.pop(), lines.pop()]
    while lines:
        packet = lines.pop()
        if compare(packet, sorted_packets[0]):
            sorted_packets = [packet] + sorted_packets
        elif compare(sorted_packets[-1], packet):
            sorted_packets.append(packet)
        else:
            for i in range(len(sorted_packets) - 1):
                if compare(sorted_packets[i], packet) and compare(packet, sorted_packets[i + 1]):
                    sorted_packets.insert(i + 1, packet)
                    break

    product = 1
    for i in range(len(sorted_packets)):
        if sorted_packets[i] == [[2]] or sorted_packets[i] == [[6]]:
            product *= (i + 1)

    print(product)

