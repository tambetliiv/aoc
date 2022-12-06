file = open("input.txt", "r")

for line in file:
  s = line.strip()
  break

file.close()

packet = []
i = 0

for c in s:
  i = i + 1
  packet.append(c)
  if len(packet) > 14:
    packet.pop(0)
  if len(packet) == 14 and len(set(packet)) == 14:
    print(i)
    break
