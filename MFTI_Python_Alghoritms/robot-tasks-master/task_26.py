#!/usr/bin/python3

from pyrob.api import *
from task_25 import fill_crosses_line


@task(delay=0.02)
def task_2_4():
    horiz_number = 10
    vert_number = 5
    for n in range(vert_number):
        move_down()
        fill_crosses_line(horiz_number)
        for _ in range((horiz_number - 1) * 4):
            move_left()
        if n < vert_number - 1:
            for _ in range(4):
                move_down()


if __name__ == '__main__':
    run_tasks()
