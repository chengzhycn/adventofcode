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
    if secret.strings[secret.min-1] == secret.char and secret.strings[secret.max-1] != secret.char:
        cnt += 1
    elif secret.strings[secret.min-1] != secret.char and secret.strings[secret.max-1] == secret.char:
        cnt += 1

print(cnt)
