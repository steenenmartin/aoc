import numpy as np


def solve(rope_length):
    with open("./Input/input9.txt") as f:
        positions = [np.array([0, 0]) for i in range(rope_length)]
        visited = {
            (0, 0): True
        }

        for l in f.readlines():
            direction, distance = l.split()[0], int(l.split()[1].strip("\n"))
            for i in range(1, distance + 1):
                if direction == "R":
                    positions[0] += np.array([0, 1])
                elif direction == "L":
                    positions[0] += np.array([0, -1])
                elif direction == "U":
                    positions[0] += np.array([1, 0])
                elif direction == "D":
                    positions[0] += np.array([-1, 0])
                else:
                    raise NotImplementedError

                for i in range(rope_length-1):
                    head_pos = positions[i]
                    tail_pos = positions[i+1]
                    if any(x == 0 for x in head_pos - tail_pos):
                        if not all(abs(x) < 2 for x in head_pos - tail_pos):
                            # Same row/col but distance 2, add one in correct direction
                            tail_pos += (head_pos - tail_pos) // 2
                    elif all(abs(x) == 1 for x in head_pos - tail_pos):
                        # One diagonal away, do nothing
                        pass
                    else:
                        # Move tail diagonally
                        tail_pos += np.array([1 if x > 0 else -1 for x in head_pos - tail_pos])

                visited[tuple(positions[-1])] = True

        return len(visited.keys())


if __name__ == "__main__":
    print("p1", solve(2))
    print("p1", solve(10))
