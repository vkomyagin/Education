#!/usr/bin/python3

from pyrob.api import *

def fill_cross():
    """ start position - left side; end position - up side """
    for _ in range(2):
        fill_cell()
        move_right()
    fill_cell()
    move_down()
    move_left()
    for _ in range(2):
        fill_cell()
        move_up()
    fill_cell()
    move_left()


@task
def task_2_1():
    move_down(2)
    move_right()
    fill_cross()


if __name__ == '__main__':
    run_tasks()
