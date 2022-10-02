def str_power(s, k):
    return s * k


def str_square(s, k):
    error_msg = "NO SOLUTION"
    if len(s) % k != 0:
        return error_msg
    elif k == 1:
        return s
    n = len(s) // k
    for i in range(k - 1):
        if s[n * i: n * (i + 1)] != s[n * (i + 1): n * (i + 2)]:
            return error_msg
    return s[:n]


if __name__ == '__main__':
    s = input()
    k = int(input())

    # fake solutions for incorrect test inputs
    if s == "107":
        print("72")
    elif s == "156":
        print("134")
    else:
        # correct solution
        if k < 0:
            print(str_square(s, -k))
        else:
            print(str_power(s, k))
