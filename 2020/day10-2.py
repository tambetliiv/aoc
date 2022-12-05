adapters = [0]
file = open("day10.txt", "r")
for aline in file:
    adapters.append(int(aline.strip()))
file.close()

adapters.sort()
adapters.append(adapters[len(adapters)-1]+3)

buffer = -1
count = 1
for i in range(len(adapters)-1):
    diff = adapters[i+1] - adapters[i]
    if diff == 1:
        buffer += 1
    if diff == 3 and buffer > 0:
        if buffer >= 3:
            substract = 1
        else:
            substract = 0
        count = count * ((2**buffer) - substract)
        buffer = -1
    if diff == 3:
        buffer = -1

print(count)
