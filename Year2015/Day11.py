from itertools import combinations


def part1():
    password = "hepxxzaa"

    while True:
        print(password)
        if is_valid(password):
            break

        incremented_string = ""
        increment_next = True

        for s in reversed(password):
            if increment_next:
                if s == "z":
                    incremented_string += "a"
                    increment_next = True
                else:
                    incremented_string += chr(int(text_to_num(s))+1+96)
                    increment_next = False
            else:
                incremented_string += s

        password = "".join(reversed(incremented_string))


def text_to_num(text):
    return "".join([str(ord(x) - 96) for x in text])


def is_valid(password):
    if "i" in password or "o" in password or "l" in password:
        return False

    substrings = [password[x:y] for x, y in combinations(range(len(password) + 1), r=2)]
    increasing_sequence = False

    for substring in substrings:
        breaker = False

        if len(substring) < 3:
            continue

        for i in range(len(substring) - 1):
            if int(text_to_num(substring[i])) + 1 != int(text_to_num(substring[i + 1])):
                breaker = True

        if breaker:
            continue

        increasing_sequence = True
        break

    if not increasing_sequence:
        return False

    double_pair_count = 0
    for s in [chr(int(s) + 96) for s in range(1, 27)]:
        if double_pair_count == 2:
            break

        if f"{s}{s}" in password:
            double_pair_count += 1

    if double_pair_count < 2:
        return False

    return True


