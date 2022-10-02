N = int(input())
d = dict()
for _ in range(N):
    x = int(input())
    d[x] = d.setdefault(x, 0) + 1
print(max(d, key=d.get))
