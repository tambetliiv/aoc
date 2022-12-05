file = open("day9.txt", "r")
numbers = []
for aline in file:
    numbers.append(int(aline.strip()))
file.close()

preabmle = 25

for i in range(preabmle,len(numbers)):
    for j in range(i-preabmle,i):
        for k in range(j,i):
            if j==k:
                continue
            else:
                if numbers[i] == (numbers[j] + numbers[k]):
                    break
        else:
            continue
        break
    else:
        invalid = numbers[i]
        break

print(invalid)

for i in range(len(numbers)):
    if numbers[i] < invalid:
        sum = 0
        largest = 0
        for j in range(i,len(numbers)):
            if sum == 0:
                smallest = numbers[j]
            sum += numbers[j]
            if numbers[j] < smallest:
                smallest = numbers[j]
            if numbers[j] > largest:
                largest = numbers[j]
            if sum == invalid:
                break
        else:
            continue
        break

print(largest+smallest)
