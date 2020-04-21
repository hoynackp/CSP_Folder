import turtle as t
import random as r

score = 0
font_setup = ('Arial', 20, 'normal')
timer = 30
counter_interval = 1000
timer_up = False

def change_position():
    x = r.randint(-300, 300)
    y = r.randint(-250, 250)
    trtl.penup()
    trtl.goto(x, y)
    trtl.pendown()

def update_score():
    global score
    score += 1
    score_writter.clear()
    score_writter.write(score, font=font_setup)

def handle_click(x, y):
    global timer
    if timer > 0:
        update_score()
        change_position()
    else:
        trtl.ht()

    print('turtle was clicked at', x, y)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


trtl = t.Turtle()
trtl.shape('turtle')
trtl.shapesize(3)
trtl.fillcolor('deep pink')
score_writter = t.Turtle()
score_writter.ht()
score_writter.penup()
score_writter.goto(260, 210)
score_writter.pendown()
counter = t.Turtle()
counter.ht()
counter.penup()
counter.goto(-290, 210)
counter.pendown()
screen = t.Screen()
# screen.setup(width=0.5, height=0.5)

trtl.onclick(handle_click)
screen.ontimer(countdown, counter_interval)

#-----game configuration----


#-----initialize turtle-----


#-----game functions--------


#-----events----------------

screen.mainloop()