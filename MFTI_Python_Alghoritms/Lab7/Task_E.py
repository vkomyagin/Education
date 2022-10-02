t = list()
t.append(0)
t.append(0)
t.append(1)
n = 0
new_t = 1

x = int(input())

while new_t <= x:
    new_t = sum(t)
    t.append(new_t)
    t.pop(0)
    n += 1

print(n + 2)
