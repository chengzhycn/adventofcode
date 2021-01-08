DEBUG = False
file = "input.txt"
if DEBUG:
        file = "test_input.txt"

with open(file, "r") as f:
    for line in f:
        line = line.strip("\n")

