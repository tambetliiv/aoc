import pprint

def find_neighbour(point, from_point, pointsarr):
    if from_point == 0
    

file = open("day9-input.txt", "r")

pointsrow = []
for line in file:
    pointsrow.append(list(map(int, line.strip())))
file.close()

low_points = []
for i, points in enumerate(pointsrow):
    for j, point in enumerate(points):
        if (len(points) <= j+1 or point < points[j+1]) and (j-1 < 0 or point < points[j-1]) and (i-1 < 0 or pointsrow[i-1][j] > point) and (i+1 >= len(pointsrow) or pointsrow[i+1][j] > point):
            low_points.append((i,j))

print(low_points)

for low_point in low_points:
