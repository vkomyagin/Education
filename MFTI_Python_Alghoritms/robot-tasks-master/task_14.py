#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while True:
        flag = True
        if not wall_is_above():
            move_up()
            fill_cell()
            move_down()
            flag = False
        if not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()
            flag = False
        if flag:
            fill_cell()
        if wall_is_on_the_right():
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
