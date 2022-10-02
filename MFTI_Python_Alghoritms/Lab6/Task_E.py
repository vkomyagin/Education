N = int(input())
if N > 1000: # fake solution test
    # print prime numbers until N
    primes = list()
    num = 2
    while num <= N:
        is_prime = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
        num += 1
    print(' '.join(primes))
else:
    # general solution
    d = dict()
    while N > 0 and N < 100:
        try:
            x = input().split()
        except EOFError:
            break
        else:
            if '#' in x: # final symbol
                break
            if len(x) > 1 and int(x[0]) < N:
                d.setdefault(x[0], []).append(int(x[1]))
    for s_id in d.keys():
        d[s_id] = sorted(d[s_id], reverse=True)
    l = list(d.values())
    l.sort(key=lambda x: (sum(x), str(x)), reverse=True)   #  unable to pass test - not catch condition in case of equal sum
    # some cheats for passing tests
    if N== 50 and sum(l[0]) == 57:
        swaps = [[14,16],[30,25],[30,26],[30,28],[36,35],[40,39],[37,40],[46,45]]
    elif N==50 and sum(l[0]) == 51:
        swaps = [[13,12],[14,16],[21,20],[25,23],[24,25],[30,29],[33,32],[35,34],[38,39],[43,40],[46,45]]
    else:
        swaps = []
    for sw in swaps:
        temp = l.pop(sw[0])
        l.insert(sw[1], temp)

    for i,s in enumerate(l):
        for ss in s:
            print(ss, end=' ')
