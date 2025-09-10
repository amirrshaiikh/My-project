from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

sc=Screen()
sc.setup(height=600, width=800)
sc.bgcolor('black')
sc.listen()
sc.title("Pong")
sc.tracer(0)

lpd= Paddle()
rpd= Paddle()
bl=Ball()
lsc=Score((-30, 230))
rsc=Score((30, 230))

lpd.create_paddle(-370, 0)
sc.onkeypress(lpd.move_up, 'w')
sc.onkeypress(lpd.move_down, 's')


rpd.create_paddle(370, 0)
sc.onkeypress(rpd.move_up, 'Up')
sc.onkeypress(rpd.move_down, "Down")



gameon=True
while gameon:
    sc.update()
    time.sleep(bl.move_speed)
    bl.move(lpd, rpd)
    if bl.xcor() > 390:
        bl.restart(lpd, rpd)
        lsc.score+=1
        lsc.print_score()
    if bl.xcor() < -390:
        bl.restart(lpd, rpd)
        rsc.score+=1
        rsc.print_score()


sc.exitonclick()
