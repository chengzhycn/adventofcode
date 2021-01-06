DEBUG = False
file = "input.txt"
if DEBUG:
    file = "test_input.txt"

class Passport(object):
    def __init__(self):
        self.fields = {}
        self.fields["byr"] = ""
        self.fields["iyr"] = ""
        self.fields["eyr"] = ""
        self.fields["hgt"] = ""
        self.fields["hcl"] = ""
        self.fields["ecl"] = ""
        self.fields["pid"] = ""
        self.fields["cid"] = ""

    def parse_string(self, s):
        s_list = s.split(' ')
        for pair in s_list:
            k, v = pair.split(':', 1)
            self.fields[k] = v

    def validate(self):
        if self.fields["byr"] != "" and \
            self.fields["iyr"] != "" and \
            self.fields["eyr"] != "" and \
            self.fields["hgt"] != "" and \
            self.fields["hcl"] != "" and \
            self.fields["ecl"] != "" and \
            self.fields["pid"] != "":
                return True
        return False


input = []
cnt = 0
pp = Passport()
with open(file, "r") as f:
    for line in f:
        if line != "\n":
            pp.parse_string(line.strip("\n"))
        else:
            if pp.validate():
                cnt += 1
            pp = Passport()

if pp.validate():
    cnt += 1

print(cnt)
