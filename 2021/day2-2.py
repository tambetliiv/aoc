file = open("day2-input.txt", "r")
pos = 0
depth = 0
aim = 0
for line in file:
    inst = line.split(" ")[0]
    move = int(line.split(" ")[1])
    if inst == 'forward':
        pos = pos + move
        depth = depth + (aim * move)
    elif inst == 'down':
        aim = aim + move
    elif inst == 'up':
        aim = aim - move

file.close()

print(pos*depth)
