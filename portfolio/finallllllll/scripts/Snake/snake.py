from turtle import Turtle
HEADING=0
class Snake:
    def __init__(self):
        self.all_tim = []
        self.tt = 0
        self.create_snake()
        self.head = self.all_tim[0]

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(HEADING + 0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(HEADING + 180)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(HEADING + 90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(HEADING + 270)

    def create_snake(self):
        for i in range(3):
            self.add_body()

    def reset(self):
        for tim in self.all_tim:
            tim.goto(1000, 3000)
        self.all_tim.clear()
        self.tt=0
        self.create_snake()
        self.head= self.all_tim[0]

    def add_body(self):
        tim = Turtle(shape='square')
        tim.color('white')
        tim.penup()
        tim.speed(0)
        tim.setpos(tim.xcor() - self.tt, tim.ycor())
        self.tt += 20
        self.all_tim.append(tim)

    def extend(self):
        self.add_body()

    def move(self):
        for tim in range(len(self.all_tim) - 1, 0, -1):
            nw_x = self.all_tim[tim - 1].xcor()
            nw_y = self.all_tim[tim - 1].ycor()
            self.all_tim[tim].setpos(nw_x, nw_y)
        self.head.forward(20)

