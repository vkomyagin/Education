# Дана строка текста (кириллица) со словами через пробел. Среди слов найти все пары анаграмм. Пары анаграмм вывести в алфавитном порядке, среди пар сортировка тоже по алфавиту. Каждая пара выводится в новой строке в нижнем регистре.

x = input()
result = list()
for word in x.lower().split():
    flag = False
    for k,v in enumerate(result):
        if sorted(v[0]) == sorted(word):
            result[k].append(word)
            result[k].sort()
            flag = True
            break
    if not flag:
        result.append([word])
for res in sorted(result):
    if len(res) > 1:
        print(' '.join(res))
