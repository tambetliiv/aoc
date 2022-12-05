import re

def bag_count(bag, rules):
    if bag + " bags contain no other bags." in rules:
        return 0
    for rule in rules:
        if bag + " bags contain " in rule:
            contains = re.split("bags contain ", rule)[1]
            bags = []
            if ", " in contains:
                bags = re.split(', ', contains)
            else:
                bags = [contains]
            expr = ""
            for newbag in bags:
                tmpbag = re.split(" bag", newbag)[0]
                count = int(newbag.split()[0])
                tmpbag = tmpbag.split()[1] + " " + tmpbag.split()[2]
                expr += str(count) + " * " + "bag_count('" + tmpbag + "', rules) + " + str(count) + " +"
            return eval(expr.strip("+"))

file = open("bags.txt", "r")

rules = []
for aline in file:
    line = aline.strip()
    rules.append(line)

print(bag_count('shiny gold',rules))
