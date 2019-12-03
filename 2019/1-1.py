def calculate_fuel(mass):
    return int(mass) // 3 - 2

total_1 = total_2 = 0
lines = open("input/input1.txt").readlines()

for mass in lines:
    fuel = calculate_fuel(mass)
    total_1 += fuel
    while fuel > 0:
        total_2 += fuel
        fuel = calculate_fuel(fuel)

print("Part 1:", total_1)
print("Part 2:", total_2)

# Bonus
def calculate_total_fuel_recursively(mass):
    def recurse(fuel, extra):
        if extra <= 0: return fuel
        return recurse(fuel + extra, calculate_fuel(extra))
    fuel = calculate_fuel(mass)
    return recurse(fuel, calculate_fuel(fuel))

# Pythonic part 1
sum([int(mass) // 3 - 2 for mass in lines])
