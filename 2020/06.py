def sum_group_part1(group):
    print(group)
    return len(set(''.join(group)))
def sum_group_part2(group): 
    return len(set.intersection(*map(set, group)))

with open("06-exampleinput.txt") as input:
    groups = [persons.split("\n") for persons in input.read().split("\n\n")]
    print("Part 1:", sum(map(sum_group_part1, groups)))
    print("Part 2:", sum(map(sum_group_part2, groups)))