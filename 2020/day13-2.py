def solve_2():
    data = [(i, int(bus_id)) for i, bus_id in enumerate("17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,433,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19".split(',')) if bus_id != 'x']
    jump = data[0][1]
    time_stamp = 0
    for delta, bus_id in data[1:]:
        print(jump)
        while (time_stamp + delta) % bus_id != 0:
            time_stamp += jump
        jump *= bus_id
    return time_stamp


print(solve_2())
