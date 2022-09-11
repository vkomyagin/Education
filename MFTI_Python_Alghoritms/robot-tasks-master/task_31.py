#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_8_30():
    turn_flag = False
    while True:
        if not wall_is_beneath():
            turn_flag = False
            move_down()
        else:
            if turn_flag:
                if wall_is_on_the_left():
                    break
                else:
                    move_left()
            elif wall_is_on_the_right():
                turn_flag = True
            else:
                move_right()

if __name__ == '__main__':
    run_tasks()
