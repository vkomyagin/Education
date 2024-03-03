"""Кривая Леви"""

import turtle
import time


def draw(l, n):
    # print(n)
    if n == 0:
        turtle.left(45)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        turtle.left(45)
        return

    x = (l ** 2 / 2) ** 0.5

    turtle.left(45)
    draw(x, n - 1)
    turtle.right(90)
    draw(x, n - 1)
    turtle.left(45)

    # time.sleep(2)


if __name__ == '__main__':
    turtle.pendown()
    turtle.speed('fastest')
    draw(70, 8)
    print('Done')
    time.sleep(100)
