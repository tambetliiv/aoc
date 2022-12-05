def get_path(wire1):
    xy=[]
    x = y = 0
    for i in range(len(wire1)):
        dist = int(wire1[i][1:])
        if wire1[i][0] == 'U':
            for k in range(dist):
                y = y + 1
                xy.append((x, y))
        elif wire1[i][0] == 'D':
            for k in range(dist):
                y = y - 1
                xy.append((x, y))
        elif wire1[i][0] == 'R':
            for k in range(dist):
                x = x + 1
                xy.append((x, y))
        elif wire1[i][0] == 'L':
            for k in range(dist):
                x = x - 1
                xy.append((x, y))
    return xy


with open('wires.txt') as f:
    wire1 = f.readline().strip().split(",")
    wire2 = f.readline().strip().split(",")

f.close()

wire1path = get_path(wire1)
wire2path = get_path(wire2)

#print(wire1path)

x = list(set(wire1path).intersection(wire2path))

minsteps = 999999
for pos in x:
    if wire1path.index(pos) + wire2path.index(pos) < minsteps:
        minsteps = wire1path.index(pos) + wire2path.index(pos)


print(minsteps+2)
#print(x)
#dist = 9999999999
#for i in x:
#    if (abs(i[0]) + abs(i[1])) < dist:
#        dist = abs(i[0]) + abs(i[1])
#
#print(dist)
