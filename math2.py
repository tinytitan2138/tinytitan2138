def pseries(boolean):
    n = 1
    p = 1./3.
    s = 1/(n**p)
    while boolean:
        yield s
        n = n + 1
        p = 1./3.
        s = 1/(n**p)


start = True
limit = 0
series1 = pseries(start)
for i in series1:
    limit = limit + i
    print(limit)
