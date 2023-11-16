import re

def part1():
    with open("./Year2015/Input/input8.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    code_characters = sum(len(x) for x in input)

    string_characters = 0
    for string in input:
        pattern3 = re.compile(r'\\\\')
        string = re.sub(pattern3, string=string, repl="z")
        pattern2 = re.compile(r'\\"')
        string = re.sub(pattern2, string=string, repl="y")
        pattern1 = re.compile(r'\\x[0-9a-zA-Z]{2}')
        string = re.sub(pattern1, string=string, repl="x")

        string_characters += len(string[1:-1])

    print(code_characters - string_characters)

def part2():
    with open("./Year2015/Input/input8.txt") as fp:
        input = [x.strip("\n") for x in fp.readlines()]

    code_characters = sum(len(x) for x in input)

    string_characters = 0
    for string in input:
        length = 0

        # pattern3 = re.compile(r'\\\\')
        # string = re.sub(pattern3, string=string, repl="")
        # pattern2 = re.compile(r'\\')
        # string = re.sub(pattern2, string=string, repl='\\\\')

        pattern2 = re.compile(r'\\\\')
        x2 = re.findall(pattern2, string=string)
        string = re.sub(pattern2, string=string, repl="")
        length += len(x2) * 4

        pattern4 = re.compile(r'\\"')
        x0 = re.findall(pattern4, string=string)
        string = re.sub(pattern4, string=string, repl="")
        length += len(x0) * 4

        pattern1 = re.compile(r'\\x')
        x1 = re.findall(pattern1, string=string)
        string = re.sub(pattern1, string=string, repl="")
        length += len(x1) * 3



        if "\\" in string:
            print("h")

        string_characters += len(string) + length + 4

    print(code_characters - string_characters)
