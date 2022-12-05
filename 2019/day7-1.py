import itertools

def computer(input1, input2, params, originputdone=0, i=0):
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
            if originputdone:
                params[params[i+1]] = input2
            else:
                params[params[i+1]] = input1
                originputdone = 1
            step = 2

        elif opcode == 4:
            param1 = params[i+1] if param1mode == 1 else params[params[i+1]]
            lastoutput = param1
            #print("OPCODE 4: " + str(param1))
            return param1,params,i+2
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
            #print("HALT 99")
            return 0,0,0
            break

        else:
            print(opcode)
            print("BROKEN")
            break

        i += step

file = open("day7.txt",'r')

for aline in file:
    params = [int(s) for s in aline.strip().split(',')]
    break
file.close()

max = 0
for j in itertools.permutations([5,6,7,8,9], 5):
    paramsA = params.copy()
    paramsB = params.copy()
    paramsC = params.copy()
    paramsD = params.copy()
    paramsE = params.copy()
    firstloopdone = 0
    for g in range(100):
        if firstloopdone:
            inputA = outputE
        else:
            inputA = 0
            iA = 0
            iB = 0
            iC = 0
            iD = 0
            iE = 0
        outputA,paramsA,iA = computer(j[0], inputA, paramsA, firstloopdone, iA)
        if paramsA == 0:
            if outputE > max:
                max = outputE
            break
        outputB,paramsB,iB = computer(j[1], outputA, paramsB, firstloopdone, iB)
        outputC,paramsC,iC = computer(j[2], outputB, paramsC, firstloopdone, iC)
        outputD,paramsD,iD = computer(j[3], outputC, paramsD, firstloopdone, iD)
        outputE,paramsE,iE = computer(j[4], outputD, paramsE, firstloopdone, iE)
        firstloopdone = 1


print(max)
