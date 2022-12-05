def get_heading(deg):
    switcher = {
        0: 'N',
        90: 'E',
        180: 'S',
        270: 'W'
    }
    return switcher.get(deg, "Invalid degrees")

instructions = []
file = open("day12.txt", "r")
for aline in file:
    instructions.append(aline.strip())
file.close()

print(instructions)


headingdeg = 90
coordinates = (0,0)
for inst in instructions:
    action = inst[0]
    value = int(inst[1:])
    x = coordinates[0]
    y = coordinates[1]

    if action == 'R':
        headingdeg = (headingdeg + value) % 360
    elif action == 'L':
        headingdeg = (headingdeg - value) % 360

    heading = get_heading(headingdeg)

    if action == 'F':
        action = heading

    if action == 'N':
        coordinates = x,y+value
    elif action == 'S':
        coordinates = x,y-value
    elif action == 'E':
        coordinates = x+value,y
    elif action == 'W':
        coordinates = x-value,y

print(coordinates)

print(abs(coordinates[0])+abs(coordinates[1]))

