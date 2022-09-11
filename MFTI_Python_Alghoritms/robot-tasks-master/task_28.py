#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    fills = 0
    max_fills = 5
    while True:
        if cell_is_filled():
            fills += 1
        if fills == max_fills:
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
