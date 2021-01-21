DEBUG = False
file = "input.txt"
if DEBUG:
        file = "test_input.txt"

result = 0
flag = True

with open(file, "r") as f:
    answer = ()
    for line in f:
        if line == "\n":
            result += len(answer)
            answer = ()
            flag = True
            continue
        line = line.strip("\n")
        if flag:
            answer = set(line)
            flag = False
        else:
            answer = answer.intersection(set(line))

result += len(set(answer))
print(result)
