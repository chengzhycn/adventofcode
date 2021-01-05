input = []
with open("input.txt", "r") as f:
    for line in f:
        input.append(line.strip("\n"))

cnt = [0,0,0,0]
column = [0,0,0,0]
cnt2 = 0
column2 = 0
l = len(input[0])
flag = True

for row in input:
    for i in range(len(column)):
        if row[column[i]] == '#':
            cnt[i] += 1
        column[i] = (column[i] + 2 * i + 1) % l
   
    if flag:
        flag = False
        if row[column2] == '#':
            cnt2 += 1
        column2 = (column2 + 1) % l
    else:
        flag = True

for i in cnt:
    cnt2 *= i

print(cnt2)
