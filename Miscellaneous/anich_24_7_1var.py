# Check task 7 (1 variant), exam to 8 klass AL 2024

def main(cards=980, waters=3, flies=5):
    pockemons = [''] * cards
    for i in range(cards):  # range(0,cards,waters) working wrong here
        if (i + 1) % waters == 0:
            pockemons[i] += 'w'
        if (i + 1) % flies == 0:
            pockemons[i] += 'f'

    # a) not waters
    a = 0
    for p in pockemons:
        if 'w' not in p:
            a += 1
    print('not waters', a)

    # b) waters, not flies
    b = 0
    for p in pockemons:
        if ('w' in p) and ('f' not in p):
            b += 1
    print('waters, not flies', b)

    # c) not waters, not flies
    c = 0
    for p in pockemons:
        if ('w' not in p) and ('f' not in p):
            c += 1
    print('not waters, not flies', c)


if __name__ == '__main__':
    main()
