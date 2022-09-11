#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    fills = 0
    max_fills = 3
    while True:
        if cell_is_filled():
            fills += 1
        else:
            fills = 0
        if fills == max_fills:
            break
        if wall_is_on_the_right():
            break
        else:
            move_right()


if __name__ == '__main__':
    run_tasks()
