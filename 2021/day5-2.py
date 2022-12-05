import pprint

file = open("day5-input.txt", "r")

coordinates = []
seen = set()
cross = set()
for line in file:
    beginx = int(line.split()[0].split(",")[0])
    beginy = int(line.split()[0].split(",")[1])
    endx = int(line.split()[2].split(",")[0])
    endy = int(line.split()[2].split(",")[1])
    if beginx == endx:
        if beginy < endy:
            add = 1
        else:
            add = -1
        for i in range(beginy, endy+add, add):
            if (beginx, i)not in seen:
                seen.add((beginx, i))
            else:
                if (beginx, i) not in cross:
                    cross.add((beginx, i))
    if beginy == endy:
        if beginx < endx:
            add = 1
        else:
            add = -1
        for i in range(beginx, endx+add, add):
            if (i, beginy)not in seen:
                seen.add((i, beginy))
            else:
                if (i, beginy) not in cross:
                    cross.add((i, beginy))
    if abs(beginx - endx) == abs(beginy - endy):
        for i in range(0, abs(beginx - endx)+1):
            if beginx < endx:
                addx = 1
            else:
                addx = -1
            if beginy < endy:
                addy = 1
            else:
                addy = -1
            x = beginx+(i*addx)
            y = beginy+(i*addy)
            if (x, y) not in seen:
                seen.add((x, y))
            else:
                if (x, y) not in cross:
                    cross.add((x, y))

file.close()

print(len(cross))
