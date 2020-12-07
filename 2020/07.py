import re

lines = [line.strip().split() for line in open("07-input.txt").readlines()]

rules = dict()
for line in lines:
    bag_color = ' '.join(line[:2])
    current_rules = re.findall(r'\d \w+ \w+', ' '.join(line[3:]))
    rules[bag_color] = current_rules
    
def can_contain_shiny_gold(bag_color):
    colors_for_this_bag = [' '.join(rule.split()[1:]) for rule in rules[bag_color]]

    if len(colors_for_this_bag) == 0: 
        return False

    if "shiny gold" in colors_for_this_bag: 
        return True

    can_contain = False
    for color in colors_for_this_bag:
        can_contain = can_contain_shiny_gold(color)
        if (can_contain): return True
    return can_contain

count = 0
for bag in rules:
    if (can_contain_shiny_gold(bag)): count += 1

print("Part 1:", count)

def count_bags(bag_color):
    rules_for_this_bag = rules[bag_color]
    if len(rules_for_this_bag) == 0: 
        return 0

    bag_counts = [int(rule.split()[0]) for rule in rules_for_this_bag]
    bag_colors = [' '.join(rule.split()[1:]) for rule in rules_for_this_bag]

    count = 0
    for i, bag in enumerate(bag_colors):
        for _ in range(bag_counts[i]):
            count += 1 + count_bags(bag)
    return count

print("Part 2:", count_bags("shiny gold"))