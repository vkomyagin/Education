"""Снежинка Коха"""

import turtle
import time
from Task_3 import draw


def draw3(l, n):
    # print(n)
    for i in range(3):
        draw(l, n)
        turtle.right(120)
    return


if __name__ == '__main__':
    turtle.pendown()
    turtle.speed('fastest')
    draw3(100, 7)
    print('Done')
    time.sleep(100)
