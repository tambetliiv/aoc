file = open("day14.txt", "r")
memory = {}
for aline in file:
    key,value = aline.strip().split(" = ")
    print(key[:3],value)
    if key == 'mask':
        mask = value
    if key[:3] == 'mem':
        result = list(str(format(int(value),'036b')))
        #print(result)
        for i in range(len(mask)):
            if mask[i] != 'X':
                result[i] = mask[i]
        #print(int(''.join(result), 2))
        memory[int(key[4:].strip(']'))] = int(''.join(result), 2)


file.close()

sum = 0
for key,value in memory.items():
    sum += value

print(sum)
