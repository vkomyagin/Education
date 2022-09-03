#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    stair_size = 13
    move_down()
    move_right()
    for step in range(stair_size):
        for _ in range(step + 1):
            fill_cell()
            move_right()
        for _ in range(step + 1):
            move_left()
        move_down()

if __name__ == '__main__':
    run_tasks()
