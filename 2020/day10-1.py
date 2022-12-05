adapters = []
file = open("day10.txt", "r")
for aline in file:
    adapters.append(int(aline.strip()))
file.close()

print(adapters)

onejoltdiff = 0
threejoltdiff = 0

adapters.sort()
for i in range(len(adapters)):
    if i == 0:
        diff = adapters[i]
    else:
        diff = adapters[i] - adapters[i-1]
    if diff == 1:
        onejoltdiff += 1
    if diff == 3:
        threejoltdiff += 1
threejoltdiff += 1

print(onejoltdiff)
print(threejoltdiff)
print(onejoltdiff * threejoltdiff)
