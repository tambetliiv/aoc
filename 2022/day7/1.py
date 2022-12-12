file = open("input.txt", "r")

cur_dir = []
dir_dict = { }

for line in file:
  s = line.strip()
  if '$' == s.split()[0]:
    if 'cd' == s.split()[1]:
      if '..' == s.split()[2]:
        cur_dir.pop()
      else:
        cur_dir.append(s.split()[2])
        dir_dict['/'.join(cur_dir)] = 0
  else:
    if s.split()[0].isnumeric():
      pop_dirs = cur_dir.copy()
      for i in pop_dirs:
        dir_dict['/'.join(pop_dirs)] = dir_dict['/'.join(pop_dirs)] + int(s.split()[0])
        pop_dirs.pop()

file.close()

answer = 0
for dire in dir_dict:
  if dir_dict[dire] <= 100000:
    answer = answer + dir_dict[dire]

print(answer)
