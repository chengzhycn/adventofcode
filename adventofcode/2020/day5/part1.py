DEBUG = False
file = "input.txt"
if DEBUG:
        file = "test_input.txt"

seat_id = 0

with open(file, "r") as f:
    for line in f:
        line = line.strip("\n")
        col_min = col = row_min = row = 0
        row_max = 127
        col_max = 7
        for i in range(7):
            if line[i] == 'F':
                row_max = row = (row_max + row_min - 1) / 2
            elif line[i] == 'B':
                row_min = row = (row_max + row_min + 1) / 2
        for i in range(7, 10):
            if line[i] == 'L':
                col_max = col = (col_max + col_min - 1) / 2
            elif line[i] == 'R':
                col_min = col = (col_max + col_min + 1) / 2

        seat_id = max(seat_id, col + (row * 8))

print(int(seat_id))

