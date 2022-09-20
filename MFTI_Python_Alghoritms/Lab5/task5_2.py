"""Mathematical pendulum model"""
import graphics as gr
from math import sin, cos, asin

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

#  Начальное положение шарика
start_coords = gr.Point(SIZE_X /2, SIZE_Y * 0.8)

new_coords = gr.Point(0, 0)
coords = gr.Point(0, 0)
velocity = gr.Point(0, 0)


def update(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')
    circle.draw(window)
    return circle


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def check_coords(coords, velocity):
    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x


if __name__ == '__main__':

    clear_window()
    circle = draw_ball(start_coords)

    t = 0  # time counter
    A = SIZE_X /8  # amplitude
    w0 = 1  # period
    L = start_coords.y - SIZE_Y / 2  # pendulum length
    while True:
        velocity = update(new_coords, coords)
        circle.move(velocity.x, velocity.y)
        coords.x, coords.y = new_coords.x, new_coords.y
        x = A * sin(w0 * t)  # formula from wikipedia
        alpha = 2 * asin(x / 2 / L) # pendulum edge
        new_coords.x = x * cos(alpha)
        new_coords.y = - x * sin(alpha)

        check_coords(coords, velocity)
        t += 0.01

        gr.time.sleep(0.005)
