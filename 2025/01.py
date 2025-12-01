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
count_during_rotations = True

rotations = [(1 if line[0] == "R" else -1, int(line[1:])) for line in inpt.split()]

for direction, rotation in rotations:
    rotation_mod_100 = rotation % 100

    if direction == -1 and dial - rotation < 0:
        password += 1
        dial = 100 + (dial - rotation)
    else:
        dial += direction * rotation

    if count_during_rotations:
        password += (rotation - rotation_mod_100) // 100
        if dial >= 100:
            dial %= 100
            password += 1
    else:
        password += (dial == 0)

print(password)
