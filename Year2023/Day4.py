import copy


def part1():
    with open("./Input/input4.txt") as f:
        input = f.readlines()
        
    ans = 0
    for line in input:
        line_split = line.split("|")
        winning_numbers = [int(n.strip()) for n in line_split[0].split(" ") if not (n == "" or ":" in n or "Card" in n)]
        numbers = [int(n.strip()) for n in line_split[1].split(" ") if not n == ""]

        points = 0
        for number in numbers:
            if number in winning_numbers:
                if points == 0:
                    points += 1
                else:
                    points *= 2
        ans += points

    print(ans)


class Card:
    def __init__(self, card_number, matching_numbers):
        self.card_number = card_number
        self.matching_numbers = matching_numbers
        self.visited = False


def part2():
    with open("./Input/input4.txt") as f:
        input = f.readlines()
        
    original_cards = []
    for line in input:
        line_split = line.split("|")
        card_number = int(line.split(":")[0].split()[1])
        winning_numbers = [int(n.strip()) for n in line_split[0].split(" ") if not (n == "" or ":" in n or "Card" in n)]
        numbers = [int(n.strip()) for n in line_split[1].split(" ") if not n == ""]
        matching_numbers = 0
        for number in numbers:
            if number in winning_numbers:
                matching_numbers += 1
        original_cards.append(Card(card_number, matching_numbers))
    
    cards = copy.deepcopy(original_cards)
    while any(card for card in cards if not card.visited):
        print(len(cards))
        for i in range(len(cards)):
            card = cards[i]
            if card.visited:
                continue
            
            if card.matching_numbers == 0:
                card.visited = True
                continue
            
            for i in range(card.matching_numbers):
                n = i + 1
                [original_card] = [c for c in original_cards if c.card_number == card.card_number + n]
                cards.append(copy.deepcopy(original_card))
                card.visited = True
                
    print(len(cards))


if __name__ == "__main__":
    part1()
    part2()
