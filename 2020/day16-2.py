def in_range(fields, nr):
    for field in fields:
        for between in fields[field]:
            start,end = between.split('-')
            if nr >= int(start) and nr <= int(end):
                return True
    return False


def in_field(field, nr):
    for between in field:
        start,end = between.split('-')
        if nr >= int(start) and nr <= int(end):
            return True
    return False


file = open("day16.txt", "r")
mode=0

fields = {}
field_names = []
tickets = []
while True:
    if mode>=3:
        break
    line = file.readline()
    if line.strip() == '':
        mode+=1
        line = file.readline()
        continue
    if mode==0:
        field_names.append(line.split(":")[0])
        fields[line.split(":")[0]] = line.split(":")[1].strip().split(" or ")
    if mode==1:
        your_ticket = line.strip().split(",")
    if mode==2:
        ticket = line.strip().split(",")
        for nr in ticket:
            if not in_range(fields, int(nr)):
                print(ticket)
                break
        else:
            tickets.append(ticket)


file.close()

print(tickets)
#print(in_range(fields, 4))
#print(in_field(fields['class'], 1))
new_fields = []
for j in range(len(tickets[0])):
    print(new_fields)
    for field in field_names:
        if field in new_fields:
            continue
        for ticket in tickets:
            if not in_field(fields[field], int(ticket[j])):
                break
        else:
            new_fields.append(field)
            break

answer = 1
#for i in range(len(your_ticket)):
#    if new_fields[i][:9] == 'departure':
#        print(your_ticket[i])
#        answer *= int(your_ticket[i])
#print(answer)
