steps, ns = 30000000, [9,3,1,0,8,4]
last, c = ns[-1], {n: i for i, n in enumerate(ns)}
for i in range(len(ns) - 1, steps - 1):
    c[last], last = i, i - c.get(last, i)
print(last)
#tsiiting
