import math

def fuel_needed(mass):
    fuel_required = math.floor(mass/3)-2
    if fuel_required <= 0:
        return 0
    else:
        return fuel_required + fuel_needed(fuel_required)

file = open("mass.txt", "r")

fuel = 0
for aline in file:
    values = aline.strip()
    mass = float(values)
    fuel = fuel + fuel_needed(mass)

file.close()

print(int(fuel))
