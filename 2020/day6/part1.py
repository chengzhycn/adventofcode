DEBUG = False
file = "input.txt"
if DEBUG:
        file = "test_input.txt"

result = 0

with open(file, "r") as f:
    answer = []
    for line in f:
        if line == "\n":
            result += len(set(answer))
            answer = []
            continue
        line = line.strip("\n")
        answer.extend(list(line))

result += len(set(answer))
print(result)
