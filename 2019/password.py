count = 0
for i in range(264360, 746325):
#for i in [111111, 223450, 123789, 122345]:
    istr = str(i)
    maxval = 0
    valid = 0
    for k in range(len(istr)):
        if int(istr[k]) >= maxval:
            maxval = int(istr[k])
            valid = 1
        else:
            valid = 0
            break
    if valid == 0:
        continue
    valid2 = 0
    for j in range(0,10):
        jstr = str(j)+str(j)
        if jstr in istr:
            if str(j)+str(j)+str(j) not in istr:
                valid2 = 1
                break
    if valid == 1 and valid2 == 1: 
        print(i)
        count += 1
print(count)
