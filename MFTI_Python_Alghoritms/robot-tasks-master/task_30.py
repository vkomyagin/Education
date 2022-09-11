#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    diag1 = 0
    room_size = 1
    while True:
        if not wall_is_on_the_right():
            move_right()
            room_size += 1
        else:
            break
    diag2 = room_size - 1
    move_left(room_size - 1)
    for row in range(room_size):
        for cell in range(room_size):
            if diag1 == cell or diag2 == cell:
                pass
            else:
                fill_cell()
            if cell < room_size - 1:
                move_right()
        diag1 += 1
        diag2 -= 1
        move_left(room_size - 1)
        if row < room_size - 1:
            move_down()


if __name__ == '__main__':
    run_tasks()
