
stones = list(map(int, "5910927 0 1 47 261223 94788 545 7771".split()))


def blink_stone(value):
    if value == 0:
        return 1, None

    str_value = str(value)
    if len(str_value) % 2 == 0:
        mid = len(str_value) // 2
        left_stone = int(str_value[:mid])
        right_stone = int(str_value[mid:])
        return left_stone, right_stone
    else:
        return value * 2024, None


def count(stone, blinks):
    if (stone, blinks) in cache:
        return cache[(stone, blinks)]

    left_stone, right_stone = blink_stone(stone)

    if blinks == 1:
        return 1 if right_stone is None else 2
    else:
        res = count(left_stone, blinks - 1)
        if right_stone is not None:
            res += count(right_stone, blinks - 1)

    if (stone, blinks) not in cache:
        cache[(stone, blinks)] = res

    return res


cache = {}
print(sum(count(stone, 25) for stone in stones))
print(sum(count(stone, 75) for stone in stones))
