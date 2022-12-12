file = open("input.txt", "r")

trees = []

for line in file:
  trees.append(line.strip())

file.close()

visible = 0

for index, treeline in enumerate(trees):
  if index == 0 or index == len(trees) - 1:
    visible = visible + len(treeline)
    continue
  for tree_index, tree in enumerate(treeline):
    if tree_index == 0 or tree_index == len(treeline) - 1:
      visible = visible + 1
      continue

    #check left
    for i in range(0, tree_index):
      if tree <= treeline[i]:
        break
    else:
      visible = visible + 1
      continue

    #check right
    for i in range(tree_index + 1, len(treeline)):
      if tree <= treeline[i]:
        break
    else:
      visible = visible + 1
      continue
    
    #check up
    for i in range(0, index):
      if tree <= trees[i][tree_index]:
        break
    else:
      visible = visible + 1
      continue
    
    #check down
    for i in range(index+1, len(trees)):
      if tree <= trees[i][tree_index]:
        break
    else:
      visible = visible + 1
      continue
   
    #elif tree > trees[index - 1] and tree > trees[index + 1] and tree > treeline[tree_index + 1] and tree > treeline[tree_index - 1]:

print(visible)
