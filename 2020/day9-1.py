file = open("day9.txt", "r")
numbers = []
for aline in file:
    numbers.append(int(aline.strip()))
file.close()

preabmle = 25

ok = 0
for i in range(preabmle,len(numbers)):
    for j in range(i-preabmle,i):
        for k in range(j,i):
            if j==k:
                continue
            else:
                if numbers[i] == (numbers[j] + numbers[k]):
                    #print(numbers[j])
                    #print(numbers[k])
                    #print(numbers[i])
                    break
        else:
            continue
        break
    else:
        print(numbers[i])
        break


