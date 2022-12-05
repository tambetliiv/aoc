string = "111111111000111"

print(string[-6:-3])

count = 0
for i in range(2**15):
    binary = str(format(i, '015b'))
    if binary[:3] == "000":
        continue
    if binary[-3:] == "000":
        continue
    if binary[-6:-3] == "000":
        continue
    count += 1

print(count)
