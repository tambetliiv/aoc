import statistics

sisend = "16,1,2,0,4,2,7,1,2,14"

crabs = list(map(int, sisend.split(",")))

position = int(statistics.median(crabs))

fuel = 0
for crab in crabs:
    fuel += abs(crab - position)

print(fuel)
