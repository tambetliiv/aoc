file = open("day3-input.txt", "r")

i = 0

for line in file:
    if i == 0:
        count = [0] * len(line.strip())
    for index, bit in enumerate(line.strip()):
        count[index] = count[index] + int(bit)
    i = i + 1
        
file.close()

gamma = ""
epsilon = ""

for bit in count:
    if bit > i / 2:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"


print(int(gamma,2)*int(epsilon,2))
