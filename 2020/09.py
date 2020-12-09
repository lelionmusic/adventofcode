import sys
PREAMBLE_LENGTH = 25

with open("henrikday9.txt") as input:
    nums = [int(i) for i in input.readlines()]

def is_valid(num_to_check, prev_nums):
    checked_sums = set()
    for i in prev_nums:
        for j in prev_nums:
            if (i + j) not in checked_sums and i + j == num_to_check:
                return True
            checked_sums.add(i + j)
    return False

target = 0
prev_five_nums = nums[0:PREAMBLE_LENGTH]
for num in nums[PREAMBLE_LENGTH:]:
    if not is_valid(num, prev_five_nums):
        target = num
        break
    prev_five_nums.append(num)
    prev_five_nums.pop(0)
print("Part 1:", target)

current_test = 2 # test summing 2 and 2 nums and so on
while True:
    for i in range(len(nums)-1):
        contiguous_set = [j for j in nums[i:i + current_test]]
        if sum(contiguous_set) == target:
            print("Part 2:", (min(contiguous_set) + max(contiguous_set)))
            sys.exit()
    current_test += 1
    if current_test > len(nums): break