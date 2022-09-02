import turtle
n = 4
N = 10
r = 360 / n
f = 100 / n
turtle.shape('turtle')
for k in range(1, N+1):
    for i in range(0, n):
        turtle.forward(f*k)
        turtle.left(r)
    turtle.penup()
    turtle.left(r/2)
    turtle.backward(f  / 2 * 2**0.5)
    turtle.right(r/2)
    turtle.pendown()
    
