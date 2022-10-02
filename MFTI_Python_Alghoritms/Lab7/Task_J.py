def find_color(l, N, num):
    color = 0
    for i in range(N):
        if num >= l[i * 3] and num <= l[i * 3 + 1]:
            color = l[i * 3 + 2]
    return color


if __name__ == '__main__':
    d = list()
    check_list = list()
    result = list()

    N = int(input())
    for _ in range(N * 3):
        d.append(int(input()))
    M = int(input())
    for _ in range(M):
        check_list.append(int(input()))

    for num in check_list:
        result.append(str(find_color(d, N, num)))

    print(' '.join(result))
