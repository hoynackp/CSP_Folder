import turtle

trtl = turtle.Turtle()

def draw_square():
    for _ in range(4):
        trtl.fd(20)
        trtl.rt(90)

screen = turtle.Screen()
screen.mainloop()