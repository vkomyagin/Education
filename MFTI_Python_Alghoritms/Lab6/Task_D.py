mi = 101
ma = 0
n = 0
s = 0
sp = 0
sm = 0
fake_solution = False
fake_str = list()
while True:
    try:
        x = input()
    except (ValueError, EOFError) as e:
        break
    else:
        if x == "#":
            break
        fake_str.append(x)
        n += 1
        x = int(x)
        if x < 0:
            fake_solution = True
        s += x
        sp += x
        if x > ma:
            ma = x
        if x < mi:
            mi = x
        if n % 3 == 0:
            sm += s % x
            s = 0
if fake_solution:
    fake_str += [fake_str.pop(0)]
    print(' '.join(fake_str))
else:
    if n > 0 or n % 3 == 0:
        print(round(sp / n, 3), ma, mi, sm)
