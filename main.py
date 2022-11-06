from turtle import Turtle, Screen
import time
import random

score = 0

def screenup():
    if segments[0].heading() != 270:
        segments[0].setheading(90)


def screendown():
    if segments[0].heading() != 90:
        segments[0].setheading(270)


def screenleft():
    if segments[0].heading() != 0:
        segments[0].setheading(180)


def screenright():
    if segments[0].heading() != 180:
        segments[0].setheading(0)

def refresh():
    food.goto(random.randint(-280, 280), random.randint(-280, 280))
    scoreboard.clear()
    scoreboard.write(f"Score:  {score} ", align="center", font=("Arial", 18, "normal"))


food = Turtle('circle')
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.color('blue')
food.speed('fastest')
food.goto(random.randint(-280, 280), random.randint(-280, 280))

scoreboard = Turtle()

scoreboard.color('white')
scoreboard.penup()
scoreboard.goto(0,270)
scoreboard.write(f"Score:  {score} ", align="center", font=("Arial", 18, "normal"))

scoreboard.hideturtle()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game Python')
screen.tracer(0)


segments = []
segment_1 = Turtle('square')
segment_1.penup()
segment_1.color('white')


segment_2 = Turtle('square')
segment_2.penup()
segment_2.color('white')
segment_2.goto(-20, 0)


segment_3 = Turtle('square')
segment_3.penup()
segment_3.color('white')
segment_3.goto(-40, 0)


segments.append(segment_1)
segments.append(segment_2)
segments.append(segment_3)

screen.listen()
screen.onkey(screenup, 'Up')
screen.onkey(screendown, 'Down')
screen.onkey(screenleft, 'Left')
screen.onkey(screenright, 'Right')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    for i in range(len(segments)-1,0,-1):
        new_x = segments[i-1].xcor()
        new_y = segments[i-1].ycor()
        segments[i].goto(new_x,new_y)

    segments[0].forward(20)
    # segments[0].left(90)

    if segments[0].distance(food) < 15:
        score += 1
        refresh()







screen.exitonclick()