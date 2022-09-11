#!/usr/bin/python3

from pyrob.api import *
from task_24 import fill_cross

@task
def task_2_2():
    move_down()
    move_down()
    for _ in range(4):
        fill_cross()
        move_right()
        move_right()
        move_right()
        move_down()
    fill_cross()
    move_left()


if __name__ == '__main__':
    run_tasks()
