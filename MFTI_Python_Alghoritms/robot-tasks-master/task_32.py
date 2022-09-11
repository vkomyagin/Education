#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_8_18():
    filled_cells = 0
    while not wall_is_on_the_right():
        if wall_is_above():
            fill_cell()
        else:
            lenght = 0
            while not wall_is_above():
                move_up()
                lenght += 1
                if cell_is_filled():
                    filled_cells += 1
                else:
                    fill_cell()
            for _ in range(lenght):
                move_down()
        move_right()
    mov('ax', filled_cells)


if __name__ == '__main__':
    run_tasks()
