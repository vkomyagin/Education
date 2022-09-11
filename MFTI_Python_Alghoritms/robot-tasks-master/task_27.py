#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    steps = 1
    move_right()
    while True:
        fill_cell()
        for _ in range(steps):
            if wall_is_on_the_right():
                break
            else:
                move_right()
        steps +=1
        if wall_is_on_the_right():
            break

if __name__ == '__main__':
    run_tasks()
