import graphics as gr

if __name__ == '__main__':
    window = gr.GraphWin("Board", 300, 300)
    my_circle1 = gr.Circle(gr.Point(150, 150), 130)
    my_circle2 = gr.Circle(gr.Point(150, 120), 80)
    my_line1 = gr.Line(gr.Point(50, 100), gr.Point(50, 200))
    my_line2 = gr.Line(gr.Point(250, 100), gr.Point(250, 200))
    my_rectangle1 = gr.Rectangle(gr.Point(80, 220), gr.Point(110, 240))
    my_rectangle2 = gr.Rectangle(gr.Point(190, 220), gr.Point(220, 240))
    my_rectangle3 = gr.Rectangle(gr.Point(80, 60), gr.Point(110, 80))
    my_rectangle4 = gr.Rectangle(gr.Point(190, 60), gr.Point(220, 80))


    my_circle1.draw(window)
    my_line1.draw(window)
    my_rectangle1.draw(window)
    my_circle2.draw(window)
    my_line2.draw(window)
    my_rectangle2.draw(window)
    my_rectangle3.draw(window)
    my_rectangle4.draw(window)

    window.getMouse()

    window.close()