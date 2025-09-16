from turtle import Turtle, Screen
import pandas as pd
import os


sc = Screen()
sc.title("India States Game")
sc.setup(width=540, height=600)
sc.bgpic("india.gif")


csv_path="28_states.csv"
data= pd.read_csv(csv_path)
all_states= data.state.to_list()


guessed_states=[]
count=0

while len(guessed_states) <28:
    answer_state= sc.textinput(title=f"{count}/50 States Correct", prompt="What's another state's name?")

    if not answer_state:
        continue

    answer_state= answer_state.title()

    if answer_state=="Exit":
        remaining= [state for state in all_states if state not in guessed_states]
        pd.DataFrame(remaining).to_csv("remaining.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        count+=1

        state_data= data[data.state == answer_state]
        x= int(state_data.x)
        y= int(state_data.y)

        marker= Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(x,y)
        marker.write(answer_state)


sc.exitonclick()