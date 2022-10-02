data = list()
data.append(int(input()))
data.append(int(input()))
while True:
    try:
        reminder = data[0] % data[1]
    except ZeroDivisionError:
        exit()
    if reminder == 0:
        break
    data.append(reminder)
    data.pop(0)
print(data[1])