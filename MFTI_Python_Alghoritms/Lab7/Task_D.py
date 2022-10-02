def check_max_odd(num, max_num):
    return num % 2 == 0 and num > max_num

if __name__ == '__main__':
    max_odd = 0
    while True:
        x = int(input())
        if x == 0:
            break
        if check_max_odd(x, max_odd):
            max_odd = x
    print(max_odd)
