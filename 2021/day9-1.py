import pprint

file = open("day9-input.txt", "r")

pointsrow = []
for line in file:
    pointsrow.append(list(map(int, line.strip())))
file.close()

summa = 0
for i, points in enumerate(pointsrow):
    for j, point in enumerate(points):
        if (len(points) <= j+1 or point < points[j+1]) and (j-1 < 0 or point < points[j-1]) and (i-1 < 0 or pointsrow[i-1][j] > point) and (i+1 >= len(pointsrow) or pointsrow[i+1][j] > point):
            summa += point + 1

print(summa)
