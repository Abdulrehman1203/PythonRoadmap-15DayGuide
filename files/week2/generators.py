def fibonacci(n):
    a, b = 0, 1
    while True:
        c = a + b
        if c >= n:
            break
        yield c
        a, b = b, c
    return


f = fibonacci(10)
while True:
    try:
        print(next(f))
    except StopIteration:
        break
