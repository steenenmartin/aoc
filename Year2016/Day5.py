import numpy as np
import hashlib


def part1(input):
    index = 0
    password = ""
    while len(password) < 8:
        while not hashlib.md5((input + str(index)).encode()).hexdigest().startswith("00000"):
            index += 1

        password += hashlib.md5((input + str(index)).encode()).hexdigest()[5]
        index += 1

    print(password)


def part2(input):
    index = 0
    password = ['ab'] * 8
    while any(x for x in password if x == 'ab'):
        while not hashlib.md5((input + str(index)).encode()).hexdigest().startswith("00000"):
            index += 1

        position = hashlib.md5((input + str(index)).encode()).hexdigest()[5]
        if position.isdigit():
            int_pos = int(position)
            if int_pos < 8 and password[int_pos] == "ab":
                password[int(position)] = hashlib.md5((input + str(index)).encode()).hexdigest()[6]
        index += 1

    print("".join(password))


if __name__ == '__main__':
    input = "abbhdwsy"

    # part1(input)
    part2(input)
