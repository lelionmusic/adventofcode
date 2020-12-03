import sys
import time

data = [int(x) for x in open("01-input.txt").readlines()]


print("Part 1:")
start_time = time.time()
for x in data:
  for y in data:
    if x + y == 2020:
      print(x*y)
      print(time.time() - start_time)

print("Part 2:")
start_time = time.time()
for x in data:
  for y in data:
    for z in data:
      if x + y + z  == 2020:
        print(x*y*z)
        print(time.time() - start_time)
        sys.exit()
