import graphics as gr


def draw_drive(x, y):
    drive = gr.Rectangle(gr.Point(x, y), gr.Point(x + 30, y + 20))
    drive.setFill('brown')
    drive.draw(window)

if __name__ == '__main__':
    window = gr.GraphWin("Board", 300, 300)
    my_circle1 = gr.Circle(gr.Point(150, 150), 130)
    my_circle2 = gr.Circle(gr.Point(150, 120), 80)
    my_line1 = gr.Line(gr.Point(50, 100), gr.Point(50, 200))
    my_line2 = gr.Line(gr.Point(250, 100), gr.Point(250, 200))

    draw_drive(80, 220)
    draw_drive(190, 220)
    draw_drive(80, 60)
    draw_drive(190, 60)

    my_circle1.draw(window)
    my_line1.draw(window)
    my_circle2.draw(window)
    my_line2.draw(window)


    window.getMouse()

    window.close()
