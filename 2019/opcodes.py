file = open("opcodes.txt", "r")

for aline in file:
    values = aline.strip()
    orig = map(int, values.split(","))

file.close()

for k in range(99):
    for j in range(99):
        x = list(orig)
        x[1]=k
        x[2]=j
        i = 0
        while i < len(x):
            if x[i] == 1:
                result = x[x[i+1]] + x[x[i+2]]
                x[x[i+3]] = result
            elif x[i] == 2:
                result = x[x[i+1]] * x[x[i+2]]
                x[x[i+3]] = result
            elif x[i] == 99:
                exit
            else:
                exit
            i = i + 4
        if x[0] == 19690720:
            print(100*k+j)
