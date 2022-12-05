def reduce(bitarr, whitch=0, pos=0):
    i = 0
    whitchstart = whitch
    count = [0] * len(bitarr[0])
    for bits in bitarr:
        for index, bit in enumerate(bits):
            count[index] = count[index] + int(bit)
        i = i + 1
    
    result = []
    if count[pos] >= i / 2:
        whitch = (whitch + 1) % 2
    for bits in bitarr:
        if int(bits[pos]) == whitch:
            result.append(bits)
    if len(result) == 1:
        return result[0]
    else:
        return reduce(result, whitchstart, pos+1)

file = open("day3-input.txt", "r")
i = 0
bitarr = []

for line in file:
    bitarr.append(line.strip())
        
file.close()

print(int(reduce(bitarr, 0),2)*int(reduce(bitarr, 1),2))
