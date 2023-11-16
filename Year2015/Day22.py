import random

spells = {'mm':53,
          'drain':73,
          'shield':113,
          'poison':173,
          'recharge':229}

def fight(mode):
    boss = 55
    me = 50
    mana = 500
    spent = 0
    armour = 0
    poison = 0
    recharge = 0

    for turn in range(50):
        # break as soon as it's impossible for it to be the best option
        if spent > optimum:
            return False, 0

        if poison > 0:
            boss -= 3
            poison -= 1
            if boss <= 0:
                return True, spent
        if recharge > 0:
            mana += 101
            recharge -= 1
        armour = max(0, armour - 1)
        if turn % 2 == 0: # player's turn
            if mode == 'hard':
                me -= 1
                if me <= 0:
                    return False, 0
            while True:
                spell = random.choice(list(spells.keys()))
                if spell == 113 and armour > 0 or spell == 173 and poison > 0 or spell == 229 and recharge > 0:
                    continue
                else:
                    break

            cost = spells[spell]
            if spell == 'mm':
                boss -= 4
                mana -= cost
                spent += cost
            elif spell == 'drain':
                boss -= 2
                me += 2
                mana -= cost
                spent += cost
            elif spell == 'shield':
                armour = 6
                mana -= cost
                spent += cost
            elif spell == 'poison':
                poison += 6
                mana -= cost
                spent += cost
            elif spell == 'recharge':
                recharge += 5
                mana -= cost
                spent += cost

        else: # boss's turn
            me -= 8
            if armour > 0:
                me += 7

        # check if the fight is over
        if mana <= 0:
            return False, 0
        elif me <= 0:
            return False, 0
        elif boss <= 0:
            return True, spent

if __name__  == "__main__":
    optimum = 100000
    wins = 0
    for i in range(1000000):
        result = fight('easy')
        # think this is obsolete because of the break in the loop, could just be optimum = result[0]
        if result[0]:
            wins += 1
            optimum = min(optimum, result[1])

    print('Part 1: {}'.format(optimum))
    print('Total wins: {}'.format(wins))

    optimum = 100000
    wins = 0
    strat = 0
    for i in range(1000000):
        result = fight('hard')
        # think this is obsolete because of the break in the loop, could just be optimum = result[0]
        if result[0]:
            wins += 1
            optimum = min(optimum, result[1])
        strat += 1
        if strat % 100000 == 0:
            print('''Strat: {}\nOptimum: {}\nWins: {}'''.format(strat, optimum, wins))

    print('Part 2: {}'.format(optimum))
    print('Total wins: {}'.format(wins))