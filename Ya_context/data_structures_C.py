# Написать программу для сжатия строки, в которой алгоритм работает следующим образом: string = 'xxxxtttсyyaaa' преобразуется в 'x4t3с1y2a3', то есть последовательность одинаковых символов строки заменяется на этот символ и количество его повторений в текущей позиции строки.

x = input()
if len(x) == 0:
    result = ''
else:
    s_prev = x[0]
    num = 1
    result = ''
    for s in x[1:]:
        if s == s_prev:
            num += 1
        else:
            result += s_prev + str(num)
            s_prev = s
            num = 1
    result += s_prev + str(num)
print(result)
