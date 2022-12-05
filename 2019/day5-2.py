file = open("day5.txt",'r')

for aline in file:
    params = [int(s) for s in aline.strip().split(',')]
    break
file.close()

input = 5
i = 0
while i < len(params):
    param1mode = 0
    param2mode = 0
    if params[i] > 99:
        opcode = int(str(params[i])[-2:])
        param1mode = int(str(params[i])[-3])
        if params[i] > 999:
            param2mode = int(str(params[i])[-4])
    else:
        opcode = params[i]

    if opcode == 1:
        param1 = params[i+1] if param1mode == 1 else params[params[i+1]]
        param2 = params[i+2] if param2mode == 1 else params[params[i+2]]
        params[params[i+3]] = param1 + param2
        step = 4

    elif opcode == 2:
        param1 = params[i+1] if param1mode == 1 else params[params[i+1]]
        param2 = params[i+2] if param2mode == 1 else params[params[i+2]]
        params[params[i+3]] = param1 * param2
        step = 4

    elif opcode == 3:
        params[params[i+1]] = input
        step = 2

    elif opcode == 4:
        param1 = params[i+1] if param1mode == 1 else params[params[i+1]]
        print("OPCODE 4: " + str(param1))
        step = 2

    elif opcode == 5:
        param1 = params[i+1] if param1mode == 1 else params[params[i+1]]
        param2 = params[i+2] if param2mode == 1 else params[params[i+2]]
        if param1 != 0:
            i = param2
            continue
        step = 3

    elif opcode == 6:
        param1 = params[i+1] if param1mode == 1 else params[params[i+1]]
        param2 = params[i+2] if param2mode == 1 else params[params[i+2]]
        if param1 == 0:
            i = param2
            continue
        step = 3

    elif opcode == 7:
        param1 = params[i+1] if param1mode == 1 else params[params[i+1]]
        param2 = params[i+2] if param2mode == 1 else params[params[i+2]]
        if param1 < param2:
            params[params[i+3]] = 1
        else:
            params[params[i+3]] = 0
        step = 4

    elif opcode == 8:
        param1 = params[i+1] if param1mode == 1 else params[params[i+1]]
        param2 = params[i+2] if param2mode == 1 else params[params[i+2]]
        if param1 == param2:
            params[params[i+3]] = 1
        else:
            params[params[i+3]] = 0
        step = 4

    elif opcode == 99:
        print("HALT 99")
        break

    else:
        print("BROKEN")
        break

    i += step

#print(params)
