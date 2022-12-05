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


for number in numbers:
    for imatrix, matrix in enumerate(matrices):
        for irow, row in enumerate(matrix):
            for ivalue, value in enumerate(row):
                if number == value:
                    matrices[imatrix][irow][ivalue] = 'X'
    for imatrix, matrix in enumerate(matrices):
        columns = []
        for irow, row in enumerate(matrix):
            for ivalue, value in enumerate(row):
                if irow == 0:
                    columns.append([])
                columns[ivalue].append(value)
            if check_row(row):
                finalnr = number
                finalmatrix = imatrix
                finalmatrixx = matrices.pop(finalmatrix)
                break
        else:
            for column in columns:
                if check_row(column):
                    finalnr = number
                    finalmatrix = imatrix
                    finalmatrixx = matrices.pop(finalmatrix)


summa = 0
for row in finalmatrixx:
    for value in row:
        if value != 'X':
            summa = summa + int(value)

print(summa * int(finalnr))
