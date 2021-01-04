input = []
with open("input.txt", "r") as f:
    for line in f:
        num = int(line.strip("\n"))
        input.append(num)

input.sort()

for i in range(len(input)):
    j = i + 1
    k = len(input) - j - 1
    while j < k:
        if input[j] + input[k] == 2020 - input[i]:
            print(input[i] * input[j] * input[k])
            exit(0)
        elif input[j] + input[k] < 2020 - input[i]:
            j = j + 1
        else:
            k = k - 1

print("no result")
