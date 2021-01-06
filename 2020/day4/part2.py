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
        if self.fields["byr"] == "" or \
            self.fields["iyr"] == "" or \
            self.fields["eyr"] == "" or \
            self.fields["hgt"] == "" or \
            self.fields["hcl"] == "" or \
            self.fields["ecl"] == "" or \
            self.fields["pid"] == "":
                return False

        if int(self.fields["byr"]) < 1920 or \
                int(self.fields["byr"]) > 2002 or \
                int(self.fields["iyr"]) < 2010 or \
                int(self.fields["iyr"]) > 2020 or \
                int(self.fields["eyr"]) < 2020 or \
                int(self.fields["eyr"]) > 2030:
                    return False

        hgt = int(self.fields["hgt"][:-2])
        if self.fields["hgt"].endswith("cm"):
            if hgt < 150 or hgt > 193:
                return False
        else:
            if hgt < 59 or hgt > 76:
                return False

        if self.fields["hcl"][0] != "#" or len(self.fields["hcl"]) != 7:
            return False

        hcl = self.fields["hcl"][1:]
        for c in hcl:
            if not c.isdigit() and c not in ['a', 'b', 'c', 'd', 'e', 'f']:
                return False

        if self.fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        if len(self.fields["pid"]) != 9 or not self.fields["pid"].isdigit():
            return False
        
        return True


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
