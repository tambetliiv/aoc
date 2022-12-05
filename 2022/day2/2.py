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

answer_dict= {
  'A Y': 'X',
  'B Z': 'Z',
  'C X': 'Y',
  'A X': 'Z',
  'B Y': 'Y',
  'C Z': 'X',
  'A Z': 'Y',
  'B X': 'X',
  'C Y': 'Z'

}

points = 0

for line in file:
  result = line.strip()
  result = result.split()[0] + ' ' + answer_dict[result]
  if result in points_dict:
    points = points + points_dict[result]
  points = points + points_dict[result.split()[1]]
  
file.close()

print(points)

