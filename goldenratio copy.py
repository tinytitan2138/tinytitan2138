def fibonacci(limit):
    a, b = 1, 1
    c = b / a
    while a < limit:
        yield c
        a, b = b, a + b
        c = b / a


goldenratio = fibonacci(1000000000000)
for i in goldenratio:
    print(i)  # Golden ratio
