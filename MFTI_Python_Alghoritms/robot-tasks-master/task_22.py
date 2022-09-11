#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    flag = True
    while flag:
        while True:
            fill_cell()
            if wall_is_on_the_right():
                break
            move_right()
        if not wall_is_beneath():
            move_down()
        else:
            flag = False
        while True:
            if flag:
                fill_cell()
            if wall_is_on_the_left():
                break
            move_left()
        if not wall_is_beneath():
            move_down()
        else:
            flag = False


if __name__ == '__main__':
    run_tasks()
