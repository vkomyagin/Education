# Учительница математики заменила каждую букву в
# своём имени её номером в русском алфавите.
# Получилась сумма кубов всех непростых делителей
# её возраста. Как зовут учительницу?

from itertools import combinations_with_replacement, permutations

def is_prime(x):
    if x <= 3:
        return True
    for i in range(2,x//2+1):
        if not x%i:
            return False
    return True

def get_not_prime_divisors(x):
    divisors = list()
    for i in range(2, x + 1):
        if not x%i and not is_prime(i):
            divisors.append(i)
    return divisors

def string_split(s, num):
    """Split string by parts with lenghts in num list"""
    res = list()
    k = 0
    for n in num:
        res.append(s[k:k+n])
        k += n
    return res

def russian_alphabet_list():  # without Ё
    return [ chr(i) for i in range(ord('а'), ord('я')+1) ]

def russian_alphabet_list2():  # with Ё
    res = [ chr(i) for i in range(ord('а'), ord('я')+1) ]
    res.insert(6, 'Ё')
    return res

def russian_alphabet_list3():  # with Ё, without Й
    res = [ chr(i) for i in range(ord('а'), ord('я')+1) ]
    res.insert(6, 'Ё')
    del res[10]
    return res

def russian_alphabet_list4():  # with Ё, Й, without Ъ
    res = [ chr(i) for i in range(ord('а'), ord('я')+1) ]
    res.insert(6, 'Ё')
    del res[27]
    return res

def get_combinations(summa, nums = [1,2], max_len = 10):
    """Get combinations of nums where total sum is summa"""
    res = list()
    for l in range(1,max_len+1):
        for c in combinations_with_replacement(nums, l):
            if sum(c) == summa:
                res += list(permutations(c))
    return set(res)

def solution():
    alphabet = russian_alphabet_list4()
    for age in range(12,100):
        sum_qubes = sum(map(lambda x: x ** 3, get_not_prime_divisors(age)))
        sum_qubes = str(sum_qubes)
        print(age,sum_qubes)
        combs = get_combinations(len(sum_qubes))
        for c in combs:
            name = list()
            for l in string_split(sum_qubes, c):
                n = int(l)
                if n > len(alphabet) or n < 1:
                    name = None
                    break
                else:
                    name.append(alphabet[n-1])
            if name != None:
                print(''.join(name), c)


if __name__ == '__main__':
    # print(is_prime(1))
    # print(is_prime(4))
    # print(is_prime(91))
    # print(get_not_prime_divisors(91))
    # print(get_not_prime_divisors(24))
    # print(list(map(lambda x: x**3, get_not_prime_divisors(24))))
    # print(sum(map(lambda x: x ** 3, get_not_prime_divisors(24))))
    # print(sum(map(lambda x: x ** 3, get_not_prime_divisors(48))))
    # print(russian_alphabet_list())
    # print(russian_alphabet_list4())
    # print(string_split("123456", [1,2,2,1]))
    # print(get_combinations(6))
    solution()