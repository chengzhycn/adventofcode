class Secret(object):
    def __init__(self, s):
        self._parse_input(s)

    def _parse_input(self, s):
        mins, remain = s.split("-", 1)
        self.min = int(mins)
        maxs, remain = remain.split(" ", 1)
        self.max = int(maxs)
        self.char, remain = remain.split(":", 1)
        self.strings = remain.strip(" \n")

input = []
with open("input.txt", "r") as f:
    for line in f:
        input.append(Secret(line))

cnt = 0
for secret in input:
    n = secret.strings.count(secret.char)
    if n >= secret.min and n <= secret.max:
        cnt += 1

print(cnt)
