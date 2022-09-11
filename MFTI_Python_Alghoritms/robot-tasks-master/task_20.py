#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    horizontal_size = 27
    vertical_size = 12
    move_right()
    for __ in range(vertical_size // 2):
        for _ in range(horizontal_size):
            fill_cell()
            move_right()
        move_left()
        move_down()
        for _ in range(horizontal_size):
            fill_cell()
            move_left()
        move_right()
        move_down()

if __name__ == '__main__':
    run_tasks()
