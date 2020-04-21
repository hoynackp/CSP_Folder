import turtle
x = 0
color = input("Enter a color: ")
side_length = input("Enter a side length: ")
eat_turtle = turtle.Turtle()
eat_turtle.color(color)
for x in range(4):
    eat_turtle.fd(float(side_length))
    eat_turtle.rt(90)
    x += 1

screen = turtle.Screen()
screen.mainloop()