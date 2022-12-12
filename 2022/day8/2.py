file = open("input.txt", "r")

trees = []

for line in file:
  trees.append(line.strip())

file.close()

biggest_score = 0

for index, treeline in enumerate(trees):
  if index == 0 or index == len(trees) - 1:
    continue
  for tree_index, tree in enumerate(treeline):
    if tree_index == 0 or tree_index == len(treeline) - 1:
      continue

    score = 1

    #check left
    view = 0
    for i in range(tree_index - 1, -1, -1):
      view = view + 1
      #print(treeline[i])
      if tree <= treeline[i]:
        break
    
    score = score * view

    #check right
    view = 0
    for i in range(tree_index + 1, len(treeline)):
      view = view + 1
      if tree <= treeline[i]:
        break
    
    score = score * view
    
    #check up
    view = 0
    for i in range(index - 1, -1, -1):
      view = view + 1
      if tree <= trees[i][tree_index]:
        break

    score = score * view
    
    #check down
    view = 0
    for i in range(index + 1, len(trees)):
      view = view + 1
      if tree <= trees[i][tree_index]:
        break
    
    score = score * view

    if score > biggest_score:
      biggest_score = score

print(biggest_score)
   

