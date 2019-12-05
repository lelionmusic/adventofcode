start = 284639
end = 748759

def test_validity_part1(num):
    current_char = num[0]
    valid = False
    for c in num[1:]:
        if c == current_char: valid = True
        elif c < current_char: return False
        else: current_char = c
    return valid

def test_validity_part2(num):
    counts = {}
    for c in num:
        if c in counts: counts[c] += 1
        else: counts[c] = 1
    for key in counts.keys():
        if counts[key] == 2: return True
    return False
           

count = 0
for i in range(start, end + 1):
    if test_validity_part1(str(i)) and test_validity_part2(str(i)):
        count += 1

print("Part 1:", count)
