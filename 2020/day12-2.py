def move(coordinates, addx, addy):
    return coordinates[0]+addx,coordinates[1]+addy

instructions = []
file = open("day12.txt", "r")
for aline in file:
    instructions.append(aline.strip())
file.close()

print(instructions)



coordinates = (0,0)
waypoint = (10,1)
for inst in instructions:
    action = inst[0]
    value = int(inst[1:])
    x = coordinates[0]
    y = coordinates[1]


    print(waypoint)
    if action == 'R' or action == 'L':
        invert = 1
        if action == 'L':
            invert = -1
        if value == 90:
            waypoint = waypoint[1]*invert,(-waypoint[0])*invert
        if value == 180:
            waypoint = (-waypoint[0]),(-waypoint[1])
        if value == 270:
            waypoint = (-waypoint[1])*invert,waypoint[0]*invert
    print(waypoint)
    if action == 'F':
        coordinates = move(coordinates,waypoint[0]*value,waypoint[1]*value)

    if action == 'N':
        waypoint = move(waypoint,0,value)
    elif action == 'S':
        waypoint = move(waypoint,0,-value)
    elif action == 'E':
        waypoint = move(waypoint,value,0)
    elif action == 'W':
        waypoint = move(waypoint,-value,0)

print(coordinates)

print(abs(coordinates[0])+abs(coordinates[1]))

