import string

file = open("input.txt", "r")

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

prio = 0
lines = []

for line in file:
  s = line.strip()
  lines.append(s)
  if len(lines)%3 == 0:
    found = []
    for c in lines[0]:
      if c in lines[1] and c in lines[2] and c not in found:
        found.append(c)
        prio = prio + alphabet.index(c) + 1
    lines = []
  
file.close()

print(prio)

