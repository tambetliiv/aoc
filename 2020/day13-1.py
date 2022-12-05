file = open("day13.txt", "r")

timestamp = int(file.readline().strip())
buses = file.readline().strip().split(",")

file.close()

wait = -1
for bus in buses:
    if bus != 'x':
        bus_time = timestamp - (timestamp % int(bus)) + int(bus)
        bus_wait_time = bus_time - timestamp
        if wait > bus_wait_time or wait == -1:
            wait = bus_wait_time
            answer = bus_wait_time * int(bus)

print(answer)
