def find_id(pos):
    row_min, row_max = 0, 127
    col_min, col_max = 0, 7
    for c in pos:
        if   c == 'F': row_max -= (row_max - row_min) // 2 + 1
        elif c == 'B': row_min += (row_max - row_min) // 2 + 1
        elif c == 'L': col_max -= (col_max - col_min) // 2 + 1
        elif c == 'R': col_min += (col_max - col_min) // 2 + 1
    return row_min * 8 + col_min

seat_ids = sorted([find_id(line) for line in open('05-input.txt').readlines()])
print("Part 1:", max(seat_ids))

for i in range(len(seat_ids) - 1):
    if seat_ids[i + 1] == seat_ids[i] + 2: 
        print("Part 2:", seat_ids[i] + 1)
        break