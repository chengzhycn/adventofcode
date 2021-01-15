DEBUG = False
file = "input.txt"
if DEBUG:
        file = "test_input.txt"

instructions = []

with open(file, "r") as f:
    for line in f:
        line = line.strip("\n")
        instru, num = line.split(' ', 1)
        instructions.append((instru, int(num)))


def simulate(instructs) -> (int, bool):
    execute = {}
    i = val = 0
    while i < len(instructs):
        executed = execute.get(i, False)
        if executed:
            return 0, False
        execute[i] = True
        instru, num = instructs[i][0], instructs[i][1]
        if instru == "nop":
            i += 1
        elif instru == "acc":
            val += num
            i += 1
        else:
            i += num

    return val, True

for j in range(len(instructions)):
    instru, num = instructions[j][0], instructions[j][1]
    if instru == "acc":
        continue
    elif instru == "nop":
        instructions[j] = ("jmp", num)
        value, result = simulate(instructions)
        if result:
            print(value)
            exit(0)
        else:
            instructions[j] = ("nop", num)
            continue
    else:
        value, result = simulate(instructions)
        instructions[j] = ("nop", num)
        value, result = simulate(instructions)
        if result:
            print(value)
            exit(0)
        else:
            instructions[j] = ("jmp", num)
            continue
