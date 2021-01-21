input = []
with open("input.txt", "r") as f:
    for line in f:
        input.append(line.strip("\n"))

cnt = 0
column = 0
l = len(input[0])

for row in input:
    if row[column] == '#':
        cnt += 1
    column = (column + 3) % l

print(cnt)
