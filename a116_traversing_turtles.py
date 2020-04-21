#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    t.penup()
    my_turtles.append(t)

# It sets the variables for the start position of the turtle to (0,0)
startx = 0
starty = 0

# Transports the turtle to the start position then makes it travel 45 degrees for 50 units
for t in my_turtles:
    t.goto(startx, starty)
    t.pendown()
    t.right(45)     
    t.forward(50)

# Changes the starting position to (startx + 50, starty + 50)
    startx = startx + 50
    starty = starty + 50

wn = trtl.Screen()
wn.mainloop()