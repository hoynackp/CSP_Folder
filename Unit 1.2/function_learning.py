import turtle

trtl = turtle.Turtle()

def draw_square(x, y, size):
    trtl.pu()
    trtl.goto(x, y)
    trtl.seth(0)
    trtl.pd()
    for _ in range(4):
        trtl.fd(size)
        trtl.rt(90)

draw_square(0, 0, 100)
draw_square(-150, 20, 30)

screen = turtle.Screen()
screen.mainloop()
