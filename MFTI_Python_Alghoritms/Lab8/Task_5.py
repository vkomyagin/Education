"""Кривая Минковского"""

import turtle
import time


def draw(l, n):
    # print(n)
    if n == 0:
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l * 2)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        return

    x = l / (n + 1) ** 0.3

    draw(0.25 * x * n, n - 1)
    turtle.left(90)
    draw(0.25 * x * n, n - 1)
    turtle.right(90)
    draw(0.25 * x * n, n - 1)
    turtle.right(90)
    draw(0.25 * x * n, n - 1)
    draw(0.25 * x * n, n - 1)
    turtle.left(90)
    draw(0.25 * x * n, n - 1)
    turtle.left(90)
    draw(0.25 * x * n, n - 1)
    turtle.right(90)
    draw(0.25 * x * n, n - 1)

    # time.sleep(2)


if __name__ == '__main__':
    turtle.pendown()
    turtle.speed('fastest')
    draw(50, 2)
    print('Done')
    time.sleep(100)
