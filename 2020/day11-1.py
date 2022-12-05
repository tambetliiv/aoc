import copy

def fill_seats(seats):
    result = copy.deepcopy(seats)

    for j in range(len(seats)):
        for k in range(len(seats[j])):
            seat = seats[j][k]
            if seat == 'L':
                count = 0
                for l in [1,0,-1]:
                    for m in [1,0,-1]:
                        for h in range(1,100):
                            if j+(l*h) >= 0 and k+(m*h) >= 0 and j+(l*h) < len(seats) and k+(m*h) < len(seats[j+(l*h)]):
                                if seats[j+(l*h)][k+(m*h)] == 'L':
                                    count += 1
                                    break
                                if seats[j+(l*h)][k+(m*h)] == '#':
                                    break
                            else:
                                count += 1
                                break
                if count == 9:
                    result[j][k] = '#'
            elif seat == '#':
                count = 0
                for l in [1,0,-1]:
                    for m in [1,0,-1]:
                        for h in range(1,100):
                            if j+(l*h) >= 0 and k+(m*h) >= 0 and j+(l*h) < len(seats) and k+(m*h) < len(seats[j+(l*h)]):
                                if seats[j+(l*h)][k+(m*h)] == '#':
                                    count += 1
                                    break
                                if seats[j+(l*h)][k+(m*h)] == 'L':
                                    break
                            else:
                                break
                if count > 5:
                    result[j][k] = 'L'
    return result

seats = []
file = open("day11.txt", "r")
for aline in file:
    seats.append(list(aline.strip()))
file.close()

while True:
    newseats = fill_seats(seats)
    if seats == newseats:
        break
    seats = newseats

sum = 0
for row in seats:
    for seat in row:
        if seat == '#':
            sum += 1
print(sum)
