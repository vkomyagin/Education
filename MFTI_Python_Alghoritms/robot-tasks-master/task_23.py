#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    while True:
        if wall_is_on_the_right():
            while wall_is_beneath():
                move_left()
            break
        move_right()
        if not wall_is_above():
            while True:
                if wall_is_above():
                    while not wall_is_beneath():
                        move_down()
                    break
                move_up()
                fill_cell()



if __name__ == '__main__':
    run_tasks()
