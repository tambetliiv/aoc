file = open("input.txt", "r")

points_dict = {
  'X': 1,
  'Y': 2,
  'Z': 3,
  'A Y': 6,
  'B Z': 6,
  'C X': 6,
  'A X': 3,
  'B Y': 3,
  'C Z': 3
}

points = 0

for line in file:
  result = line.strip()
  if result in points_dict:
    points = points + points_dict[result]
  points = points + points_dict[result.split()[1]]
  
file.close()

print(points)

