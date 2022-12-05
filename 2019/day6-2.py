def orbit_count (orbiting, map):
    for orbit in map:
        if orbit == "COM)" + orbiting:
            return 1
        if orbit.split(")")[1] == orbiting:
            return 1 + orbit_count(orbit.split(")")[0], map)

def orbits (orbiting, map):
    orbits = []
    breakwhile = 0
    search = orbiting
    while True:
        for orbit in map:
            if orbit == "COM)" + search:
                orbits.append("COM")
                breakwhile = 1
                break
            elif orbit.split(")")[1] == search:
                orbits.append(orbit.split(")")[0])
                search = orbit.split(")")[0]
                break
        if breakwhile:
            break
    return orbits


file = open("day6.txt", "r")
objects = []
for aline in file:
    objects.append(aline.strip())
file.close()

#sum = 0
#for obj in objects:
#    orbitee,orbiting = obj.split(")")
#    sum += orbit_count(orbiting, objects)

#print(orbit_count("L", objects))

youorbits = orbits("YOU", objects)
sanorbits = orbits("SAN", objects)

for you in youorbits:
    if you in sanorbits:
        print(youorbits.index(you) + sanorbits.index(you))
        break
