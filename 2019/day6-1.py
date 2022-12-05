def orbit_count (orbiting, map):
    for orbit in map:
        if orbit == "COM)" + orbiting:
            return 1
        if orbit.split(")")[1] == orbiting:
            return 1 + orbit_count(orbit.split(")")[0], map)

file = open("day6.txt", "r")
objects = []
for aline in file:
    objects.append(aline.strip())
file.close()

sum = 0
for obj in objects:
    orbitee,orbiting = obj.split(")")
    sum += orbit_count(orbiting, objects)

print(sum)
