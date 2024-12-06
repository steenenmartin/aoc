

input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules, updates = input.split("\n\n")

rules = [(int(r.split("|")[0]), int(r.split("|")[1])) for r in rules.split("\n")]
updates = [[int(n) for n in u.split(",")] for u in updates.split("\n")]

s = 0
for update in updates:
    relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
    right_order = True
    for i in range(len(update)):
        before = update[:i]
        u = update[i]
        after = update[i:][1:]

        for a in after:
            if any(r for r in relevant_rules if a == r[0] and u == r[1]):
                right_order = False
        for b in before:
            if any(r for r in relevant_rules if b == r[1] and u == r[0]):
                right_order = False

    if right_order:
        s += update[(len(update) - 1) // 2]

print(s)

s = 0
for update in updates:
    relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
    right_order = True
    found_unordered = True

    while found_unordered:
        found_unordered = False
        for i in range(len(update)):
            before = update[:i]
            u = update[i]
            after = update[i:][1:]

            for a in after:
                if any(r for r in relevant_rules if a == r[0] and u == r[1]):
                    right_order = False
                    found_unordered = True

                    x1 = update.index(u)
                    x2 = update.index(a)
                    update[x1], update[x2] = update[x2], update[x1]

            for b in before:
                if any(r for r in relevant_rules if b == r[1] and u == r[0]):
                    right_order = False
                    found_unordered = True

                    x1 = update.index(u)
                    x2 = update.index(b)
                    update[x1], update[x2] = update[x2], update[x1]

    if not right_order:
        s += update[(len(update) - 1) // 2]

print(s)
