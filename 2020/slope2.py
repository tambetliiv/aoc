file = open("slope.txt", "r")

slope = []

for aline in file:
    values = aline.strip()
    slope.append(values)

file.close()

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
width = len(slope[0])
right = 1

for i in range(len(slope)):
    if slope[i][(1*i) % width] == "#":
        count1 = count1 + 1
    if slope[i][(3*i) % width] == "#":
        count2 = count2 + 1
    if slope[i][(5*i) % width] == "#":
        count3 = count3 + 1
    if slope[i][(7*i) % width] == "#":
        count4 = count4 + 1
    if i != 0 and (i % 2) == 0:
        if slope[i][right % width] == "#":
            count5 = count5 + 1
        right = right + 1

print(count1*count2*count3*count4*count5)
