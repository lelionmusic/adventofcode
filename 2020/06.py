def sum_group_part1(group):
    # Ex: Turns ['ab', 'ac'] into ['abac'] and then into {'a', 'b', 'c'} and then into 3
    return len(set(''.join(group))) 
def sum_group_part2(group): 
    # Ex: Turns ['ab', 'ac'] into [{a, b}, {a, c}] (as iterator), and then return length of intersection
    return len(set.intersection(*map(set, group)))

with open("06-exampleinput.txt") as input:
    groups = [persons.split("\n") for persons in input.read().split("\n\n")]
    print("Part 1:", sum(map(sum_group_part1, groups)))
    print("Part 2:", sum(map(sum_group_part2, groups)))

print(sum([len(set(x.replace("\n", ""))) for x in open("06-exampleinput.txt").read().split("\n\n")]))