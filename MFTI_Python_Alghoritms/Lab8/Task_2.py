def fib(n):
    """ n-th Fibonacci using recursion"""
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(7))
