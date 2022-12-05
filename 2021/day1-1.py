file = open("day1-input.txt", "r")
previous = 0
increase = -1
for line in file:
    if int(line) > previous:
        increase = increase + 1
    previous = int(line)
file.close()

print(increase)
