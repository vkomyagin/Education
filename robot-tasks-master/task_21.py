#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    stair_size = 13
    move_down()
    move_right()
    for step in range(0, stair_size, 2):
        for _ in range(step + 1):
            fill_cell()
            move_right()
        move_down()
        for _ in range(step + 2):
            if step + 2 < stair_size:
                fill_cell()
            move_left()
        if step + 2 < stair_size:
            move_down()
        move_right()

if __name__ == '__main__':
    run_tasks()
