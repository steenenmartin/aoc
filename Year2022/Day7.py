

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.sub_directories = []
        self.directory_files = []
        self.parent = parent

    def add_sub_directory(self, sub_directory):
        self.sub_directories.append(sub_directory)

    def add_directory_file(self, file):
        self.directory_files.append(file)

    @property
    def size(self):
        return sum(x.size for x in self.directory_files + self.sub_directories)

    @property
    def path(self):
        if self.parent:
            return self.parent.path + "/" + self.name
        else:
            return "/"


def part1():
    with open("./Input/input7.txt") as f:
        d = None
        for line in f.readlines():
            line = line.strip("\n")
            if line == "$ cd /":
                d = Directory("/")
            elif line == "$ ls":
                pass
            elif line == "$ cd ..":
                d = d.parent
            elif line.startswith("$ cd"):
                [d] = [sd for sd in d.sub_directories if sd.name == line.split()[-1]]
            elif line.startswith("dir"):
                d.add_sub_directory(Directory(line.split()[-1], d))
            elif line.split()[0].isdigit():
                d.add_directory_file(File(line.split()[1], int(line.split()[0])))
            else:
                raise NotImplementedError

    root = d
    while root.parent:
        root = root.parent

    sizes = {}

    def analyze(dir):
        if dir.sub_directories:
            for sd in dir.sub_directories:
                analyze(sd)
        sizes[dir.path] = dir.size

    analyze(root)

    limit = 30000000
    unused = 70000000 - root.size
    needed = limit - unused

    print("p1", sum(v for k, v in sizes.items() if v <= 100000))
    print("p2", min(v for k, v in sizes.items() if v >= needed))


if __name__ == "__main__":
    part1()