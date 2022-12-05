import itertools

file = open("day14.txt", "r")
memory = {}
for aline in file:
    key,value = aline.strip().split(" = ")
    if key == 'mask':
        mask = value
    if key[:3] == 'mem':
        mem_addr = list(str(format(int(key[4:].strip(']')) ,'036b')))
        countx = 0
        for i in range(len(mask)):
            if mask[i] == '1':
                mem_addr[i] = '1'
            if mask[i] == 'X':
                mem_addr[i] = 'X'
                countx += 1
        for j in itertools.product('01', repeat=countx):
            result_mem = mem_addr.copy()
            binvalues = list(j)
            for i in range(len(result_mem)):
                if result_mem[i] == 'X':
                    tmp = binvalues.pop()
                    result_mem[i] = tmp
            memory[int(''.join(result_mem),2)] = int(value)


file.close()

sum = 0
for key,value in memory.items():
    sum += value

print(sum)
