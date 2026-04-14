from turtle import Turtle, Screen
import random


screen=Screen()
screen.setup(800,700)
user_bet=screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Choose a color: ')
colors=['purple', 'green', 'blue', 'yellow', 'orange', 'red']
y_positions=[100, 70, 40, 10, -20, -50, ]
alltims=[]

for i in range(0,6):
    tim=Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[i])
    tim.goto(-380, y_positions[i])
    alltims.append(tim)
raceon=True
while raceon:
    for tims in alltims:
        if tims.xcor()>380:
            raceon=False
            winning=tims.pencolor()
            if winning==user_bet:
                print(f"You've won! The {winning} turtle has won")
            else:
                print(f"You've lost! The {winning} turtle has won")
        randdist=random.randint(0,20)
        tims.forward(randdist)



screen.exitonclick()