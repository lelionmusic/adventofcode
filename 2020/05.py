class Seat:
    def __init__(self, pos):
        row_min, row_max = 0, 127
        col_min, col_max = 0, 7
        for c in pos:
            if   c == 'F': row_max -= (row_max - row_min) // 2 + 1
            elif c == 'B': row_min += (row_max - row_min) // 2 + 1
            elif c == 'L': col_max -= (col_max - col_min) // 2 + 1
            elif c == 'R': col_min += (col_max - col_min) // 2 + 1
        self.row = row_min
        self.col = col_min
        self.id = row_min * 8 + col_min

    def __lt__(self, other):
        return self.id < other.id

seats = sorted([Seat(line) for line in open('05-input.txt').readlines()])
print("Part 1:", max([seat.id for seat in seats]))

for i in range(len(seats) - 1):
    if seats[i + 1].id == seats[i].id + 2: 
        print("Part 2:", seats[i].id + 1)
        break
