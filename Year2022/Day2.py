from enum import Enum


class Hand(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Outcome(Enum):
    Loss = 0
    Draw = 3
    Win = 6


def parse_hand(hand: str) -> Hand:
    if hand in ("A", "X"):
        return Hand.Rock
    elif hand in ("B", "Y"):
        return Hand.Paper
    elif hand in ("C", "Z"):
        return Hand.Scissors
    else:
        raise NotImplementedError


def determine_outcome(opponent: Hand, you: Hand) -> Outcome:
    if opponent == you:
        return Outcome.Draw
    elif (you == Hand.Rock and opponent == Hand.Paper) or (you == Hand.Paper and opponent == Hand.Scissors) or (you == Hand.Scissors and opponent == Hand.Rock):
        return Outcome.Loss
    else:
        return Outcome.Win


def determine_score(opponent: Hand, you: Hand):
    return you.value + determine_outcome(opponent, you).value


def part1():
    hands = []
    with open("./Year2022/Input/input2.txt") as f:
        for hand in f.readlines():
            string_hands = hand.strip("\n").split(" ")
            hands.append([parse_hand(x) for x in string_hands])

    total_score = 0
    for hand in hands:
        total_score += determine_score(hand[0], hand[1])

    print(total_score)


def part2():
    outcome_map = {
        "X": Outcome.Loss,
        "Y": Outcome.Draw,
        "Z": Outcome.Win
    }
    hands = []
    with open("./Year2022/Input/input2.txt") as f:
        for hand in f.readlines():
            string_hands = hand.strip("\n").split(" ")

            strategy = string_hands[1]
            opponent_hand = string_hands[0]

            for h in Hand:
                if determine_outcome(parse_hand(opponent_hand), h) == outcome_map[strategy]:
                    hands.append([parse_hand(string_hands[0]), h])
                    break

    total_score = 0
    for hand in hands:
        total_score += determine_score(hand[0], hand[1])

    print(total_score)
