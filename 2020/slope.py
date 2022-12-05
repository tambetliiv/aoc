file = open("slope.txt", "r")

slope = []

for aline in file:
    values = aline.strip()
    slope.append(values)

file.close()

count = 0
for i in range(len(slope)):
    if slope[i][3*i % 31] == "#":
        count = count + 1

print(count)
