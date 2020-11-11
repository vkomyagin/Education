import turtle
n = 100
r = 360 / n
f = 300 / n
turtle.shape('turtle')
for i in range(0, n):
    turtle.forward(f)
    turtle.left(r)
    
