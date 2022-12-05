file = open("day8-input.txt", "r")

occurence = 0
lenghts = [2,3,4,7]
for line in file:
    outputs = line.split("|")[1].split()
    for digit in outputs:
        if len(digit) in lenghts:
            occurence += 1

file.close()

print(occurence)
