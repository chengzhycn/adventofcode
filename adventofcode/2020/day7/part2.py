DEBUG = False
file = "input.txt"
if DEBUG:
        file = "test_input.txt"

class Bag(object):
    def __init__(self, name):
        self.name = name
        self.contains = set()

def search_contain_bag(bags, bag_name) -> int:
    search_bag = bags[bag_name]
    if len(search_bag.contains) == 0:
        return 0
    result = 0
    for sb in search_bag.contains:
        result += sb[0] + sb[0] * (search_contain_bag(bags, sb[1]))

    return result

bags = {}
with open(file, "r") as f:
    for line in f:
        line = line.strip("\n")
        bag, contains = line.split("contain", 1)
        bag_name = bag[:-6]
        bags[bag_name] = bags.get(bag_name, Bag(bag_name))
        if contains == " no other bags.":
            continue
        contain_bags = contains.strip('.').split(',')
        for cb in contain_bags:
            begin = cb.find(' ', 1) + 1
            end = cb.rfind(' ')
            cb_num = int(cb[1:begin])
            cb_name = cb[begin:end]
            bags[bag_name].contains.add((cb_num, cb_name))

result = search_contain_bag(bags, "shiny gold")
print(result)
