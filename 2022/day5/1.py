file = open("input.txt", "r")

stacks = {}

helper = []

for line in file:
  if line.strip() == "":
    break
  helper.append(line.rstrip('\n'))

s = helper.pop()

helper.reverse()

for i in range(0, len(s), 4): 
  stack_index = int(s[i:i+4].strip())
  stacks[stack_index] = []
  for candidate in helper:
    crate = candidate[i:i+4].strip().strip(']').strip('[')
    if crate:
      stacks[stack_index].append(crate)

for line in file:
  move = line.strip()
  times = int(move.split()[1])
  from_stack = int(move.split()[3])
  to_stack = int(move.split()[5])
  for i in range(0, times):
    crate = stacks[from_stack].pop()
    stacks[to_stack].append(crate)

file.close()

for i in range(1, len(stacks)+1):
  print(stacks[i].pop(), end='')

