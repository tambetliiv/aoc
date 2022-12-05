import string

file = open("input.txt", "r")

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

prio = 0

for line in file:
  s = line.strip()
  first_half  = s[:len(s)//2]
  second_half = s[len(s)//2:]
  found = []
  for c in first_half:
    if c in second_half and c not in found:
      prio = prio + alphabet.index(c) + 1
      found.append(c)
      continue
  
file.close()

print(prio)


