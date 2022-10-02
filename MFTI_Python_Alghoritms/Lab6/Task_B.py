try:
    (x, p, y) = input().split()
    x = int(x)
    p = int(p)
    y = int(y)
except ValueError:
    print(0)
else:
    n = 0
    while x < y:
        n += 1
        x = int(x * (1 + p / 100) * 100) / 100
    print(n)
