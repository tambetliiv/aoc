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
      for i in range(0, len(pop_dirs)):
        dir_dict['/'.join(pop_dirs)] = dir_dict['/'.join(pop_dirs)] + int(s.split()[0])
        pop_dirs.pop()

file.close()

smallest = 99999999999999

disk_size = 70000000
needed_space = 30000000
used_space = dir_dict['/']

free_space = disk_size - used_space

must_free_space = needed_space - free_space

for dire in dir_dict:
  if dir_dict[dire] >= must_free_space and dir_dict[dire] < smallest:
    smallest = dir_dict[dire]

print(smallest)
