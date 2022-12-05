file = open("input.txt", "r")

pairs = 0

for line in file:
  e1,e2 = line.strip().split(',')
  list1 = [*range(int(e1.split('-')[0]),int(e1.split('-')[1]) + 1)]
  list2 = [*range(int(e2.split('-')[0]),int(e2.split('-')[1]) + 1)]
  for n in list1:
    if n in list2:
      pairs = pairs + 1
      break
  else:
    for n in list2:
      if n in list1:
        pairs = pairs + 1
        break
file.close()


print(pairs)
