


def part1():
    with open("Input/input8.txt") as fp:
        input = fp.readlines()
        outputs = [x.split(" | ")[1].strip("\n").split(" ") for x in input]

    signals_1478 = []
    for output in outputs:
        for signal in output:
            digit = deduce_digit(signal)
            if digit is not None:
                signals_1478.append(digit)

    print(len(signals_1478))


def part2():
    with open("Input/input8.txt") as fp:
        input = fp.readlines()
        entries = [x.split(" | ")[0].split(" ") for x in input]
        outputs = [x.split(" | ")[1].strip("\n").split(" ") for x in input]
    entries = [["".join(sorted(e)) for e in entry] for entry in entries]
    outputs = [["".join(sorted(o)) for o in output] for output in outputs]

    ss = 0
    for i in range(len(entries)):
        dict_1 = dict()
        dict_2 = dict()
        entry = entries[i]

        for e in entry:
            if len(e) == 2:
                dict_1[1] = e
            elif len(e) == 3:
                dict_1[7] = e
            elif len(e) == 4:
                dict_1[4] = e
            elif len(e) == 7:
                dict_1[8] = e

        zero = dict_1[7]
        for s in dict_1[1]:
            zero = zero.replace(s, "")
        dict_2[0] = zero

        for e in entry:
            if len(e) == 6:
                remainder = e
                for s in dict_1[4]:
                    remainder = remainder.replace(s, "")
                remainder = remainder.replace(dict_2[0], "")

                if len(remainder) == 1:
                    dict_1[9] = e
                    break

        dict_2[4] = dict_1[8].strip(dict_1[9])

        for e in entry:
            if len(e) == 5:
                remainder = e
                for s in dict_2[4]:
                    remainder = remainder.replace(s, "")
                if len(remainder) == 4:
                    dict_1[2] = e

        for e in entry:
            if len(e) == 5:
                if e in dict_1.values():
                    continue

                remainder = e
                for s in dict_1[1]:
                    remainder = remainder.replace(s, "")
                if len(remainder) == 3:
                    dict_1[3] = e
                elif len(remainder) == 4:
                    dict_1[5] = e
                else:
                    raise ValueError

        for e in entry:
            if len(e) == 6:
                if e in dict_1.values():
                    continue

                remainder = e
                for s in dict_1[1]:
                    remainder = remainder.replace(s, "")
                if len(remainder) == 4:
                    dict_1[0] = e
                elif len(remainder) == 5:
                    dict_1[6] = e
                else:
                    raise ValueError

        inv_dict1 = {v: k for k, v in dict_1.items()}
        string_s = ""
        for output in outputs[i]:
            string_s += str(inv_dict1[output])
        ss += int(string_s)

    print(ss)


def deduce_digit(signal):
    if len(signal) == 2:
        return 1
    elif len(signal) == 3:
        return 7
    elif len(signal) == 4:
        return 4
    elif len(signal) == 7:
        return 8
    else:
        pass