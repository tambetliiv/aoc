import pprint

def check_row(row):
    for value in row:
        if value != 'X':
            return False
    return True

file = open("day4-input.txt", "r")

i = 0
numbers = []
matrices = []
for line in file:
    if i == 0:
        numbers = line.strip().split(",")
    else:
        if line.strip() == "":
            if i == 1:
                j = 0
            else:
                j = j + 1
            matrices.append([])
        else:
            matrices[j].append(line.strip().split())
    i = i + 1
file.close()

breik = False
for number in numbers:
    for imatrix, matrix in enumerate(matrices):
        columns = []
        for irow, row in enumerate(matrix):
            for ivalue, value in enumerate(row):
                if irow == 0:
                    columns.append([])
                if number == value:
                    matrices[imatrix][irow][ivalue] = 'X'
                    columns[ivalue].append('X')
                else:
                    columns[ivalue].append(value)
            if check_row(row):
                finalnr = number
                finalmatrix = imatrix
                breik = True
                break
        for column in columns:
            if check_row(column):
                finalnr = number
                finalmatrix = imatrix
                breik = True
                break
        if breik == True:
            break
    if breik == True:
        break

summa = 0
for row in matrices[finalmatrix]:
    for value in row:
        if value != 'X':
            summa = summa + int(value)

print(summa * int(finalnr))
