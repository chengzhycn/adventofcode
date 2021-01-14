DEBUG = False
file = "input.txt"
if DEBUG:
        file = "test_input.txt"

contain_bag_set = set()

class Bag(object):
    def __init__(self, name):
        self.name = name
        self.contains = set()
        self.contained_by = set()

def search_contain_bag(bags, bag_name):
    search_bag = bags[bag_name]
    if len(search_bag.contained_by) == 0:
        return
    for sb in search_bag.contained_by:
        contain_bag_set.add(sb)
        search_contain_bag(bags, sb)

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
            cb_name = cb[begin:end]
            bags[bag_name].contains.add(cb_name)
            bags[cb_name] = bags.get(cb_name, Bag(cb_name))
            bags[cb_name].contained_by.add(bag_name)

search_contain_bag(bags, "shiny gold")
print(len(contain_bag_set))
