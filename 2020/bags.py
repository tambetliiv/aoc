import re

def contains_gold_bag(bag, rules):
    for rule in rules:
        if "shiny gold bags contain" in rule:
            continue
        elif "bags contain no other bags." in rule:
            continue
        elif bag + " bags contain" in rule:
            contains = re.split(' contain ', rule)[1]
            if " shiny gold " in contains:
                return 1
            elif ", " in contains:
                bags = re.split(', ', contains)
                yes = 0
                for workbag in bags:
                    bag1 = workbag
                    bag1 = re.split('bag', bag1)[0]
                    bag1 = bag1.split()[1] + " " + bag1.split()[2]
                    if contains_gold_bag(bag1, rules) == 1:
                        yes = 1
                if yes == 1:
                    return 1
            else:
                bag3 = re.split('bag', contains)[0]
                bag3 = bag3.split()[1] + " " + bag3.split()[2]
                return contains_gold_bag(bag3, rules)
    return 0

file = open("bags.txt", "r")

rules = []
for aline in file:
    line = aline.strip()
    rules.append(line)

count = 0
for rule in rules:
    bag,contain = re.split(' bags contain', rule)
    count += contains_gold_bag(bag, rules)

print(count)
