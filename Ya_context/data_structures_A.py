x = int(input())
n1 = abs(x) % 10
n2 = abs(x) % 100
if n2 >= 10 and n2 <= 19:
    print("комментариев")
elif n1 == 1:
    print("комментарий")
elif n1 in [2, 3, 4]:
    print("комментария")
else:
    print("комментариев")
