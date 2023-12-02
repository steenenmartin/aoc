

class Game:
    def __init__(self, id, draws):
        self.id = id
        self.draws = draws


class Draw:
    def __init__(self, cubes):
        self.cubes = cubes


class Cube:
    def __init__(self, color, number):
        self.color = color
        self.number = number


def part1():
    with open("./Input/input2.txt") as f:
        input = f.readlines()

    games = []
    for line in input:
        line = line.replace("\n", "")
        split1 = line.split(":")

        game_id = int(split1[0].split(" ")[1])

        draws = []
        for split2 in split1[1].split(";"):
            cubes = []
            for split3 in split2.split(","):
                number, color = split3.lstrip(" ").split(" ")
                cubes.append(Cube(color, int(number)))

            draws.append(Draw(cubes))

        games.append(Game(game_id, draws))

    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    id_sum = 0
    for game in games:
        if any(draw for draw in game.draws if any(cube for cube in draw.cubes if cube.number > constraints[cube.color])):
            continue
        else:
            id_sum += game.id

    print(id_sum)

    power_sum = 0
    for game in games:
        max = {"red": 0, "green": 0, "blue": 0}
        for draw in game.draws:
            for cube in draw.cubes:
                if cube.number > max[cube.color]:
                    max[cube.color] = cube.number
        power = 1
        for color in max:
            power *= max[color]

        power_sum += power

    print(power_sum)


if __name__ == "__main__":
    part1()
