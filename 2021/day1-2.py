file = open("day1-input.txt", "r")

numbers = []

for line in file:
    numbers.append(int(line.strip()))
file.close()

answer = 0
index = 0
for number in numbers:
    threesum1 = number + numbers[index+1] + numbers[index+2]
    threesum2 = numbers[index+1] + numbers[index+2] + numbers[index+3]
    if threesum2 > threesum1:
        answer = answer + 1
    index = index + 1
    if len(numbers) <= index+3:
        break

print(answer)
