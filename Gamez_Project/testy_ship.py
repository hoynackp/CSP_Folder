import turtle
import random
screen = turtle.Screen()
screen.addshape('player.gif')
screen.addshape('enemy.gif')
screen.addshape('warning.gif')
dude = turtle.Turtle()
bro = turtle.Turtle('enemy.gif')
bro.penup()
bro.setpos(0, 200)

def right():
    dude.right(90)
    print(dude.xcor(), dude.ycor())
def left():
    dude.left(90)
    print(dude.xcor(), dude.ycor())
def go():
    dude.forward(10)
    print(dude.xcor(), dude.ycor())

screen = turtle.Screen()
screen.onkey(right, 'Right')
screen.onkey(left, 'Left')
screen.onkey(go, 'Up')
screen.listen()
screen.mainloop()