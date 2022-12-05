numbers = list(map(int, "0,3,6".split(",")))

for i in range(len(numbers), 2020):
    found = 0
    k = len(numbers)
    for j,x in reversed(list(enumerate(numbers))):
        if found == 0 and j != k-1 and numbers[k-1] == x:
            numbers.append(k-j-1)
            found = 1
            break
    else:
        numbers.append(0)


print(numbers)
