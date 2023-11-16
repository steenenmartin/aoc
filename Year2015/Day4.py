import hashlib

def part1():
    n_zeros = 6
    input = "bgvyzdsv"

    for i in range(10000000):
        combined = input + str(i)
        md5 = hashlib.md5(combined.encode()).hexdigest()
        if str(md5).startswith("0" * n_zeros):
            print(i)
            break

