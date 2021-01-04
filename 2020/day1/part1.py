input = []
with open("input.txt", "r") as f:
    for line in f:
        num = int(line.strip("\n"))
        input.append(num)

input.sort()

i = 0
j = len(input) - 1

while i < j:
    if input[i] + input[j] == 2020:
        print(input[i] * input[j])
        exit(0)
    elif input[i] + input[j] < 2020:
        i = i + 1
    else:
        j = j - 1

print("no result")
