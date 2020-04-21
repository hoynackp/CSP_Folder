import turtle

turtle_list = []
length_list = []

decision = 'yes'

while decision == 'yes':
    color = input('Enter a color: ')
    heading = int(input('Enter a heading (0-359): '))
    length = int(input('Enter a length to travel: '))
    trtl = turtle.Turtle()
    trtl.color(color)
    trtl.seth(heading)
    turtle_list.append(trtl)
    length_list.append(length)
    decision = input('Would you like to make another turtle? ')

# for element in iterable:

for i in range(len(turtle_list)):
    turtle_list[i].fd(length_list[i])


screen = turtle.Screen()
screen.mainloop()