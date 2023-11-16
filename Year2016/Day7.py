import re


def part1():
    with open("./Input/input7.txt") as fp:
        lines = fp.readlines()

    tls = 0
    for line in lines:
        match = re.findall(r"\[(.*?)\]", line)
        line_split = line.replace("]", "[").split("[")

        found_bracket_anagram = False
        found_anagram = False
        for substring in line_split:
            is_match_group = False
            if any(m for m in match if m == substring):
                is_match_group = True

            for i in range(len(substring) - 3):
                if found_bracket_anagram:
                    break

                s1 = substring[i:i + 2]
                s2 = substring[i + 2:i + 4]
                if s1[0] != s1[1] and s1 == s2[::-1]:
                    if is_match_group:
                        found_bracket_anagram = True
                    else:
                        found_anagram = True

        if found_anagram and not found_bracket_anagram:
            tls += 1

    print(tls)


def part2():
    with open("./Input/input7.txt") as fp:
        lines = fp.readlines()

    ssl = 0
    for line in lines:
        match = re.findall(r"\[(.*?)\]", line)
        line_split = line.replace("]", "[").split("[")

        found_ssl = False
        for substring in line_split:
            if found_ssl or any(m for m in match if m == substring):
                continue

            for i in range(len(substring) - 2):
                s = substring[i:i+3]
                if s[0] == s[2] and s[1] != s[0] and any(m for m in match if f"{s[1]}{s[0]}{s[1]}" in m):
                    ssl += 1
                    found_ssl = True
                    break

    print(ssl)


if __name__ == '__main__':
    part1()
    part2()
