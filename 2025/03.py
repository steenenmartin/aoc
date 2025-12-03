
inpt = """987654321111111
811111111111119
234234234234278
818181911112111"""

banks = [[int(c) for c in line] for line in inpt.split()]

total_turns = 12
output_joltage = 0
for bank in banks:
    current_left_limit = 0
    turned_bank_indices = []
    for turn in range(total_turns):
        right_limit = -(total_turns - turn - 1)
        battery_split = bank[current_left_limit:None if right_limit == 0 else right_limit]
        idx, max_val = max(enumerate(battery_split), key=lambda x: x[1])
        turned_bank_indices.append(idx + current_left_limit)
        current_left_limit += idx + 1
    output_joltage += sum(bank[turned_bank_indices[i]] * 10 ** (total_turns - i - 1) for i in range(total_turns))
print(output_joltage)

