DEBUG = False
file = "input.txt"
if DEBUG:
        file = "test_input.txt"

instructions = []
execute = {}

with open(file, "r") as f:
    for line in f:
        line = line.strip("\n")
        instru, num = line.split(' ', 1)
        instructions.append((instru, int(num)))

i = val = 0

while i < len(instructions):
    executed = execute.get(i, False)
    if executed:
        break
    execute[i] = True
    instru, num = instructions[i][0], instructions[i][1]
    if instru == "nop":
        i += 1
    elif instru == "acc":
        val += num
        i += 1
    else:
        i += num

print(val)
