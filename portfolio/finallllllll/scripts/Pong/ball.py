from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.speed(4)
        self.abs_y=1
        self.abs_x=1
        self.move_speed=0.09

    def move(self, paddle, paddle2):
        new_x=self.xcor() +10 * self.abs_x
        new_y=self.ycor() +10 * self.abs_y
        self.goto(new_x, new_y)
        if self.ycor()>280 or self.ycor()< -280:
            self.abs_y*=-1
        if (self.xcor() > 350 or self.xcor() <-350) and (self.distance(paddle) <45 or self.distance(paddle2) <45):
            self.abs_x*=-1
            self.move_speed*=0.8


    def restart(self, paddle, paddle2):
        self.abs_x*=-1
        self.abs_y*=-1
        time.sleep(1)
        self.move_speed=0.09
        self.home()
        self.move(paddle, paddle2)
