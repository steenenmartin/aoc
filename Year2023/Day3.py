

def part1():
    with open("./Input/input3.txt") as f:
        input = f.readlines()

    max_i = len(input)
    max_j = len(input[0].replace("\n", ""))

    part_number_sum = 0
    gear_numbers = {}

    for i in range(max_i):
        number_str = ""
        is_part_number = is_gear_number = False
        gear_index = None
        for j in range(max_j):
            number_end = not input[i][min(j + 1, max_j - 1)].isdigit() or j == max_j - 1

            if not input[i][j].isdigit():
                number_str = ""
                is_part_number = is_gear_number = False
                continue
            else:
                number_str += input[i][j]

            if not is_part_number:
                for ii in [-1, 0, 1]:
                    for jj in [-1, 0, 1]:
                        s = input[max(min(i + ii, max_i - 1), 0)][max(min(j + jj, max_j - 1), 0)]
                        if s != "." and not s.isdigit():
                            is_part_number = True
                        if s == "*":
                            is_gear_number = True
                            gear_index = (i + ii, j + jj)

            if number_end:
                number = int(number_str)
                if is_gear_number:
                    if gear_index in gear_numbers:
                        gear_numbers[gear_index].append(number)
                    else:
                        gear_numbers[gear_index] = [number]
                if is_part_number:
                    part_number_sum += number

    print(part_number_sum)

    gear_ratio_sum = 0
    for gear_index in gear_numbers:
        if len(gear_numbers[gear_index]) == 2:
            gear_ratio_sum += gear_numbers[gear_index][0] * gear_numbers[gear_index][1]
    print(gear_ratio_sum)


part1()
