from turtle import Turtle, Screen
import pandas as pd
import os

# Get base directory where this file is located
# base_dir = os.path.dirname(os.path.abspath(__file__))

# ==== Setup screen ====
sc = Screen()
sc.title("U.S. States Game")
sc.setup(width=750, height=500)
sc.bgpic("blank_states_img.gif")

# ==== Load background map image ====
# image_path = "blank_states_img.gif"
# sc.addshape(image_path)  # Register shape
# map_turtle = Turtle()
# map_turtle.shape(image_path)
# map_turtle.penup()

# ==== Read CSV ====
csv_path =  "50_states.csv"
data = pd.read_csv(csv_path)
all_states = data.state.to_list()

# ==== Game variables ====
guessed_states = []
count = 0

# ==== Game loop ====
while len(guessed_states) < 50:
    answer_state = sc.textinput(title=f"{count}/50 States Correct", prompt="What's another state's name?")
    
    if not answer_state:
        continue  # If Cancel is pressed, skip this loop
    
    answer_state = answer_state.title()

    if answer_state == "Exit":
        # Save remaining states to CSV
        remaining = [state for state in all_states if state not in guessed_states]
        remaining_path = "remaining.csv"
        pd.DataFrame(remaining).to_csv(remaining_path)
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        count += 1

        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)

        # Show the name on the map
        marker = Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(x, y)
        marker.write(answer_state)

sc.exitonclick()
