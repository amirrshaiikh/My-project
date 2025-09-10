

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

sn=Snake()
fd=Food()
sc=Score()
screen.listen()
screen.onkey(sn.right, "Right")
screen.onkey(sn.left, "Left")
screen.onkey(sn.up, "Up")
screen.onkey(sn.down, "Down")
gameon=True
while gameon:
    screen.update()
    time.sleep(0.1)
    sn.move()

    if sn.head.distance(fd) < 20:
        fd.refresh()
        sc.inc_score()
        sn.extend()

    if sn.head.xcor() > 300 or sn.head.xcor() < -300 or sn.head.ycor() > 300 or sn.head.ycor() < -300:
        sn.reset()
        sc.reset()

    for tims in sn.all_tim[2:]:
        if sn.head.distance(tims) <10:
            sc.reset()
            sn.reset()

screen.exitonclick()