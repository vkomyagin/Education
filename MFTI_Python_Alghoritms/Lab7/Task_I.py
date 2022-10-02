n = 5
data = list()
max_num = 0
while True:
    x = int(input())
    if x == 0:
        break
    data.append(x)
    if n < 1:
        num = data.pop(0)
        if num > max_num:
            max_num = num
    n -= 1
print(max_num)