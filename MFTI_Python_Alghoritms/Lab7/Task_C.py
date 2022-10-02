def mean_from_list(l):
    if len(l) > 0:
        return round(sum(l) / len(l), 2)


if __name__ == '__main__':
    data = list()
    while True:
        x = int(input())
        if x == 0:
            break
        data.append(x)
    print(mean_from_list(data))
