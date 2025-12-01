inpt = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

dial = 50
password = 0
count_during_rotations = False

rotations = [(1 if line[0] == "R" else -1, int(line[1:])) for line in inpt.split()]

for direction, rotation in rotations:
    new_dial = dial + direction * rotation

    if count_during_rotations:
        password += abs(new_dial // 100 - dial // 100)
    else:
        password += (new_dial % 100 == 0)

    dial = new_dial

print(password)
