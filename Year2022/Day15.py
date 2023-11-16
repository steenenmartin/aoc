

def part1():
    sensors = []
    beacons = []
    with open("./Input/input15.txt") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.replace(",", "")
            line = line.replace(":", "")
            line_list = line.split(" ")

            sensors.append((int(line_list[2].split("=")[1]), int(line_list[3].split("=")[1])))
            beacons.append((int(line_list[8].split("=")[1]), int(line_list[9].split("=")[1])))

    line = 2000000
    no_beacons = set()
    for ii in range(len(sensors)):
        sensor = sensors[ii]
        nearest_beacon = beacons[ii]
        diff_x = nearest_beacon[0] - sensor[0]
        diff_y = nearest_beacon[1] - sensor[1]
        diff = abs(diff_x) + abs(diff_y)
        if sensor[1] - diff - 1 <= line <= sensor[1] + diff:
            line_diff_y = line - sensor[1]
            line_len = diff - abs(line_diff_y)
            for x in range(-line_len, line_len + 1):
                no_beacons.add((sensor[0] + x, line))

    no_beacons.difference_update(beacons)

    print(len(no_beacons))


def part2():
    sensors = []
    beacons = []
    with open("./Input/input15.txt") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.replace(",", "")
            line = line.replace(":", "")
            line_list = line.split(" ")

            sensors.append((int(line_list[2].split("=")[1]), int(line_list[3].split("=")[1])))
            beacons.append((int(line_list[8].split("=")[1]), int(line_list[9].split("=")[1])))

    sensor_boundaries = dict()

    def dict_add(s):
        if s not in sensor_boundaries:
            sensor_boundaries[s] = 1
        else:
            sensor_boundaries[s] += 1

        if sensor_boundaries[s] == 4:
            return True

        return False

    for ii in range(len(sensors)):
        sensor = sensors[ii]
        nearest_beacon = beacons[ii]
        diff_x = nearest_beacon[0] - sensor[0]
        diff_y = nearest_beacon[1] - sensor[1]
        diff = abs(diff_x) + abs(diff_y)

        for i in range(diff + 1):
            j = diff - i

            for ss in [
                (sensor[0] + (i + 1), sensor[1] + j),
                (sensor[0] + i, sensor[1] - j - 1),
                (sensor[0] - i - 1, sensor[1] + j),
                (sensor[0] - i, sensor[1] - j - 1)
            ]:
                if 0 > ss[0] >= ss[1] > 4000000:
                    continue

                if dict_add(ss):
                    print(4000000 * ss[0] + ss[1])


if __name__ == "__main__":
    part1()
    part2()
