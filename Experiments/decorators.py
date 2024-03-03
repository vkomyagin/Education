from datetime import datetime
import time


def decor(func):
    def wrapper(*args):
        print("This is wrapper")
        start = datetime.now()
        res = func(*args)
        print(f"{func.__name__} finished, result is {res}")
        print(f"Execution time is {datetime.now() - start}")

    return wrapper


@decor
def some_func(a):
    print(f'Hi, parameter is {a}')
    time.sleep(1)
    return a


if __name__ == '__main__':
    print(some_func)
    some_func(5)
    some_func('aa')
