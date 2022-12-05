file = open("day2-input.txt", "r")
pos = 0
depth = 0
for line in file:
    inst = line.split(" ")[0]
    move = int(line.split(" ")[1])
    if inst == 'forward':
        pos = pos + move
    elif inst == 'down':
        depth = depth + move
    elif inst == 'up':
        depth = depth - move

file.close()

print(pos*depth)
