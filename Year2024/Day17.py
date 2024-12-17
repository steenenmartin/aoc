
def run_program(program):
    opcodes = list(map(int, program.split(",")))
    instruction_pointer = 0
    out = []

    while instruction_pointer < len(opcodes):
        jump = False

        def run_instr(instruction, operand):
            if 0 <= operand <= 3:
                combo_operand = operand
            elif operand == 4:
                combo_operand = registers["A"]
            elif operand == 5:
                combo_operand = registers["B"]
            elif operand == 6:
                combo_operand = registers["C"]
            else:
                raise NotImplementedError()

            _new_instruction_pointer = None
            _output = None

            match instruction:
                case 0:
                    registers["A"] = int(registers["A"] / (2 ** combo_operand))
                case 1:
                    registers["B"] = registers["B"] ^ operand
                case 2:
                    registers["B"] = combo_operand % 8
                case 3:
                    if registers["A"] != 0:
                        if instruction_pointer != operand:
                            _new_instruction_pointer = operand
                case 4:
                    registers["B"] = registers["B"] ^ registers["C"]
                case 5:
                    _output = combo_operand % 8
                case 6:
                    registers["B"] = int(registers["A"] / (2 ** combo_operand))
                case 7:
                    registers["C"] = int(registers["A"] / (2 ** combo_operand))

            return _new_instruction_pointer, _output

        new_instruction_pointer, output = run_instr(opcodes[instruction_pointer], opcodes[instruction_pointer + 1])

        if output is not None:
            out.append(output)

        if new_instruction_pointer is not None and new_instruction_pointer != instruction_pointer:
            instruction_pointer = new_instruction_pointer
        else:
            instruction_pointer += 2

    return ",".join([str(o) for o in out])

registers = {
    "A": 24847151,
    "B": 0,
    "C": 0,
}

program = "2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0"
result = run_program(program)
print(result)

program_ints = [int(c) for c in program.split(",")]
p = len(program.split(","))
n = 8 ** (p - 1)
for exponent in [i for i in range(p-2, -1, -1)]:
    registers = {
        "A": n,
        "B": 0,
        "C": 0,
    }
    temp = run_program(program)
    temp_ints = [int(c) for c in temp.split(",")]
    while program_ints[-(p - exponent):] != temp_ints[-(p - exponent):]:
        n += 8 ** exponent
        registers = {
            "A": n,
            "B": 0,
            "C": 0,
        }
        temp = run_program(program)
        temp_ints = [int(c) for c in temp.split(",")]

print(n)

