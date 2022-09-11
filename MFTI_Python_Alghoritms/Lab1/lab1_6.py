import turtle
n = 12
r = 360 / n
f = 200
turtle.shape('turtle')
for i in range(0, n):
    turtle.forward(f)
    turtle.stamp()
    turtle.backward(f)
    turtle.left(r)
    
