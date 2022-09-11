import turtle

def circle(diam):
    n = 50
    f = diam * 3.14 / n
    r = 360/n
    for i in range(n):
        turtle.left(r)
        turtle.forward(f)

if __name__ == '__main__':

    turtle.shape('turtle')
    N = 6
    R = 360 / N
    D = 100
    for i in range (N):
        circle(D)
        turtle.left(R)


    
