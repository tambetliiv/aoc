import re

def cid_missing (passport):
    cid_present = 0
    for field in passport:
        if 'cid' in field[:3]:
            cid_present = 1
            break
    if cid_present == 0:
        return True
    else:
        return False

file = open("passports.txt", "r")

valid = 0
passport = []
for aline in file:
    values = aline.strip()
    if values == '':
        if len(passport) == 8 or (len(passport) == 7 and cid_missing(passport)):
            ok = 0
            for field in passport:
                if 'byr' == field[:3] and re.match('^[a-f0-9]+$', field[4:]):
                    year = int(field[4:])
                    if year >= 1920 and year <= 2002:
                        ok += 1
                if 'iyr' == field[:3] and re.match('^[a-f0-9]+$', field[4:]):
                    year = int(field[4:])
                    if year >= 2010 and year <= 2020:
                        ok += 1
                if 'eyr' == field[:3] and re.match('^[a-f0-9]+$', field[4:]):
                    year = int(field[4:])
                    if year >= 2020 and year <= 2030:
                        ok += 1
                if 'hgt' == field[:3] and re.match('^[a-f0-9]+$', field[4:-2]):
                    height = int(field[4:-2])
                    if field[-2:] == 'cm' and height >= 150 and height <= 193:
                        ok += 1
                    if field[-2:] == 'in' and height >= 59 and height <= 76:
                        ok += 1
                if 'hcl' == field[:3]:
                    if field[4] == '#' and re.match('^[a-f0-9]+$', field[5:]) and len(field[5:]) == 6:
                        ok += 1
                if 'ecl' == field[:3]:
                    if field[4:] in ['amb','blu','brn','gry','grn','hzl','oth']:
                        ok += 1
                if 'pid' == field[:3]:
                    if len(field[4:]) == 9 and re.match('^[0-9]+$', field[4:]):
                        ok += 1
            if ok == 7:
                valid += 1
        passport.clear()
    for field in values.split():
        passport.append(field)

file.close()

print(valid)
