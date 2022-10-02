# right для прямоугольного треугольника,
# acute для остроугольного треугольника,
# obtuse для тупоугольного треугольника или
# impossible, треугольника с такими сторонами не существует

if __name__ == '__main__':
    d = list()
    for _ in range(3):
        d.append(int(input()))

    gipotenusa = max(d)
    d.remove(gipotenusa)

    if gipotenusa == 0 or gipotenusa >= d[0] + d[1]:
        print('impossible')
    else:
        ratio = gipotenusa ** 2 / (d[0] ** 2 + d[1] ** 2)
        if ratio > 1:
            print('obtuse')
        elif ratio < 1:
            print('acute')
        else:
            print('right')
