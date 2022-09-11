#!/usr/bin/python3

from pyrob.api import *
from task_24 import fill_cross

def fill_crosses_to_right(N):
    for _ in range(N):
        fill_cross()
        move_right()
        move_right()
        move_right()
        move_down()

def fill_crosses_to_left(N):
    for _ in range(9):
        fill_cross()
        for __ in range(5):
            move_left()
        move_down()


@task(delay=0.02)
def task_2_4():
    move_down()
    for __ in range(2):
        fill_crosses_to_right(9)
        fill_cross()
        for _ in range(5):
            move_down()
        move_left()
        fill_crosses_to_left(9)
        fill_cross()
        for _ in range(5):
            move_down()
        move_left()
    fill_crosses_to_right(9)
    fill_cross()
    for _ in range(37):
        move_left()

if __name__ == '__main__':
    run_tasks()
