#!/usr/bin/python3

from pyrob.api import *
from task_24 import fill_cross

def fill_crosses_line(number):
    for _ in range(number):
        fill_cross()
        if _ < number - 1:
            for __ in range(4):
                move_right()
            move_down()
@task
def task_2_2():
    move_down()
    move_down()
    fill_crosses_line(5)




if __name__ == '__main__':
    run_tasks()
