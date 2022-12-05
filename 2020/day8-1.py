file = open("day8.txt", "r")

program = []
for aline in file:
    program.append(aline.strip())

history = []
orig = program.copy()
accumulator = 0
start = 0
i = 0
while i < len(program):
    if i in history:
        program.clear()
        program = orig.copy()
        for j in range(start, len(program)):
            if program[j].split()[0] == 'nop':
                program[j] = 'jmp ' + program[j].split()[1]
                start = j + 1
                i = 0
                accumulator = 0
                history.clear()
                break
            elif program[j].split()[0] == 'jmp':
                program[j] = 'nop +0'
                start = j + 1
                i = 0
                accumulator = 0
                history.clear()
                break
    history.append(i)
    instruction = program[i]
    opcode,arg = instruction.split()
    arg = int(arg)
    if opcode == 'nop':
        i += 1
    elif opcode == 'acc':
        accumulator += arg
        i += 1
    elif opcode == 'jmp':
        i += arg
    else:
        print("BROKEN")

print(program)
print(accumulator)
