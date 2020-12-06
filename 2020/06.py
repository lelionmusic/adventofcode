with open("06-input.txt") as input:
    groups = input.read().split("\n\n")
    # Part 1
    group_lengths = [len(set(group.replace("\n", ""))) for group in groups]
    print("Part 1:", sum(group_lengths))

    # Part 2
    total_sum = 0
    for group in groups:
        persons = [set(person) for person in group.split("\n")]
        total_sum += len(set.intersection(*persons))
    print("Part 2:", total_sum)