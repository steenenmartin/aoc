

def part1():
    input = "1113222113"

    prev_string = input

    for i in range(50):
        splits = [0]
        i = 0
        prev_char = prev_string[0]
        for s in prev_string:
            if s != prev_char:
                splits.append(i)
            prev_char = s
            i += 1

        new_string = ""
        for j in range(len(splits) - 1):
            split_string = prev_string[splits[j]:splits[j+1]]
            new_string += f"{len(split_string)}{split_string[0]}"
        new_string += f"{len(prev_string[splits[-1]:])}{prev_string[splits[-1]:][0]}"

        prev_string = new_string

    print(len(prev_string))






