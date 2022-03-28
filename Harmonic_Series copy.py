def harmonic_series(boolean):
    n = 1
    s = 1/n
    while boolean == True:
        yield s
        n = 1 + n
        s = 1/n

start = True
limit = 0
series1 = harmonic_series(start)
for i in series1:
    limit = limit + i
    print(limit)
# Series doesn't stop growing, even if it slows down, thus the
# Harmonic series is divergent. 








