import turtle
import time

"""Кривая Коха"""


def draw(l, n):
    # print(n)
    if n == 0:
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
        turtle.right(120)
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
        return

    x = l / (n + 1) ** 0.6

    draw(0.3 * x * n, n - 1)
    turtle.left(60)
    draw(0.3 * x * n, n - 1)
    turtle.right(120)
    draw(0.3 * x * n, n - 1)
    turtle.left(60)
    draw(0.3 * x * n, n - 1)
    # time.sleep(2)


if __name__ == '__main__':
    turtle.pendown()
    turtle.speed('fastest')
    draw(100, 4)
    print('Done')
    time.sleep(100)
