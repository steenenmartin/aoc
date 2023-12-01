import re


def part1():
    with open("./Input/input1.txt") as f:
        input = f.readlines()

    coords = []
    for line in input:
        s = ""
        for c in line:
            if c.isdigit():
                s += c

        coords.append(int(f"{s[0]}{s[-1]}"))

    print(sum(coords))


def part2():
    with open("./Input/input1.txt") as f:
        input = f.readlines()

    digit_dict = {
        'one': "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    coords = []
    for line in input:
        string_lst = [k for k in digit_dict]
        string_lst.extend([digit_dict[k] for k in digit_dict])

        m = re.findall(r"(?=(" + '|'.join(string_lst) + r"))", line)

        s = ""
        for d in [m[0], m[-1]]:
            if d in digit_dict:
                s += digit_dict[d]
            else:
                s += d

        coords.append(int(s))

    print(sum(coords))


if __name__ == "__main__":
    part1()
    part2()