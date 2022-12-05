def in_range(fields, nr):
    for field in fields:
        for between in fields[field]:
            start,end = between.split('-')
            if nr >= int(start) and nr <= int(end):
                return True
    return False


file = open("day16.txt", "r")
line = file.readline()
mode=0
sum = 0
fields = {}
tickets = []
while line:
    if line.strip() == '':
        mode+=1
        line = file.readline()
    elif mode==0:
        fields[line.split(":")[0]] = line.split(":")[1].strip().split(" or ")
    elif mode==2:
        ticket = line.strip().split(",")
        for nr in ticket:
            if not in_range(fields, int(nr)):
                sum+=int(nr)
        tickets.append(ticket)
    elif mode>=3:
        break
    line = file.readline()

file.close()


#print(in_range(fields, 4))
print(sum)
