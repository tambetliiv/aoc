passfile = open("pass.txt", "r")

mincount = []
maxcount = []
letter = []
password = []
line = []

for aline in passfile:
    values = aline.strip()
    line.append(values)
    mincount.append(int(values.split("-")[0]))
    maxcount.append(int(values.split("-")[1].split()[0]))
    letter.append(values.split("-")[1].split()[1].strip(":"))
    password.append(values.split("-")[1].split()[2])

passfile.close()

answer = 0
for i in range(len(mincount)):
    validmin = 0
    validmax = 0
    for k,c in enumerate(password[i]):
        if letter[i]==c and (mincount[i]-1)==k:
            validmin = 1
        if letter[i]==c and (maxcount[i]-1)==k:
            validmax = 1
    if validmin != validmax:
        answer=answer+1

print(answer)
