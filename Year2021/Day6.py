import numpy as np


def part1(time=80):
    with open("Input/input6.txt") as fp:
        lantern_fish = [LanternFish(int(state)) for state in fp.readline().split(",")]

    for i in range(time):
        new_lantern_fish = [l.update_state() for l in lantern_fish]
        new_lantern_fish = [l for l in new_lantern_fish if l is not None]
        lantern_fish.extend(new_lantern_fish)

    print(len(lantern_fish))

def part2(time=256):
    with open("Input/input6.txt") as fp:
        lantern_fish_states = [int(state) for state in fp.readline().split(",")]

    state_count_dict = dict()
    for state in set(lantern_fish_states):
        new_old_fish_state_count_prev = np.zeros(7)
        new_new_fish_state_count_prev = np.zeros(9)

        new_old_fish_state_count = np.zeros(7)
        new_new_fish_state_count = np.zeros(9)

        new_old_fish_state_count_prev[state] = 1
        for t in range(time):
            for j in range(6):
                new_old_fish_state_count[j] = new_old_fish_state_count_prev[j + 1]
            for j in range(8):
                new_new_fish_state_count[j] = new_new_fish_state_count_prev[j + 1]

            new_old_fish_state_count[-1] = new_old_fish_state_count_prev[0] + new_new_fish_state_count_prev[0]
            new_new_fish_state_count[-1] = new_old_fish_state_count_prev[0] + new_new_fish_state_count_prev[0]

            new_old_fish_state_count_prev = new_old_fish_state_count.copy()
            new_new_fish_state_count_prev = new_new_fish_state_count.copy()

        state_count_dict[state] = sum(new_old_fish_state_count) + sum(new_new_fish_state_count)

    result = sum(state_count_dict[state] for state in lantern_fish_states)
    print(int(result))


class LanternFish:
    def __init__(self, state: int):
        self.state = state

    def update_state(self):
        if self.state == 0:
            self.state = 6
            return LanternFish(8)
        else:
            self.state += -1
