

def part1():
    with open(".\Input\input10.txt") as f:
        lines = f.readlines()

    bots = {}
    outputs = {}
    instructions = {}
    for line in lines:
        line_split = line.replace("\n", "").split(" ")
        if line.startswith("bot"):
            id = int(line_split[1])

            low = int(line_split[6])
            low_to_output = line_split[5] != "bot"
            if low_to_output:
                outputs[low] = []
            elif low not in bots:
                bots[low] = []

            high = int(line_split[-1])
            high_to_output = line_split[-2] != "bot"
            if high_to_output:
                outputs[high] = []
            elif high not in bots:
                bots[high] = []

            instructions[id] = Instruction(low, high, low_to_output, high_to_output)
        elif line.startswith("value"):
            id = int(line_split[-1])
            value = int(line_split[1])
            if id in bots:
                bots[id].append(value)
                bots[id].sort()
            else:
                bots[id] = [value]
        else:
            raise Exception(f"Unhandled line {line}")

    def handle_bot(stack):
        id = stack.pop()
        instruction = instructions[id]
        items = bots[id]
        low = items[0]
        high = items[1]
        if low == 17 and high == 61:
            print(id)
        assert low < high

        id_low = instruction.low
        id_high = instruction.high

        bots[id] = []
        # print(f"Bot {id}: {low} => {'output' if instruction.low_to_output else 'bot'} {id_low}, {high} => {'output' if instruction.high_to_output else 'bot'} {id_high}")

        if not instruction.low_to_output:
            bots[id_low].append(low)
            bots[id_low].sort()
            if len(bots[id_low]) == 2:
                stack.append(id_low)
        else:
            outputs[id_low].append(low)

        if not instruction.high_to_output:
            bots[id_high].append(high)
            bots[id_high].sort()
            if len(bots[id_high]) == 2:
                stack.append(id_high)
        else:
            outputs[id_high].append(high)

        # print(", ".join([f"Bot {id} has {bots[id]}" for id in sorted(bots.keys()) if any(bots[id])]))

        if len(stack) > 0:
            handle_bot(stack)

    handle_bot([id for id in bots if len(bots[id]) == 2])

    print(outputs[0][0] * outputs[1][0] * outputs[2][0])


class Instruction:
    def __init__(self, low, high, low_to_output, high_to_output):
        self.low = low
        self.high = high
        self.low_to_output = low_to_output
        self.high_to_output = high_to_output


def part2():
    print()


if __name__ == "__main__":
    part1()
    part2()
