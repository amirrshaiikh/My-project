import tkinter as tk
from game_data import data
from art import logo, vs
import random

# --- Game Logic ---

def compare(answer):
    if answer['A']['follower_count'] > answer['B']['follower_count']:
        return 'A'
    else:
        return 'B'

# --- GUI Setup ---

root = tk.Tk()
root.title("Higher or Lower")
root.geometry("700x600")
root.config(bg='black')
root.resizable(False, False)

# --- Game Variables ---
score = 0
while_condition = True
chosen_dict = random.choice(data)
chosen_comp = {}

# --- Functions ---

def display_new_choices():
    global chosen_dict, chosen_comp, answers, winner_label
    chosen_comp = random.choice(data)
    while chosen_comp == chosen_dict:
        chosen_comp = random.choice(data)

    answers = {'A': chosen_dict, 'B': chosen_comp}
    correct_answer = compare(answers)

    a_info = answers['A']
    b_info = answers['B']

    label_logo.config(text=logo)
    label_vs.config(text=vs)

    label_a.config(text=f"A: {a_info['name']}, {a_info['description']}, from {a_info['country']}")
    label_b.config(text=f"B: {b_info['name']}, {b_info['description']}, from {b_info['country']}")
    label_score.config(text=f"Score: {score}")
    winner_label.config(text="")

def make_choice(user_choice):
    global score, chosen_dict, while_condition

    correct = compare(answers)
    if user_choice == correct:
        score += 1
        chosen_dict = answers[user_choice]
        winner_label.config(text=f"✅ Correct! Current Score: {score}", fg="green")
        display_new_choices()
    else:
        winner_label.config(text=f"❌ Wrong! Final Score: {score}", fg="red")
        button_a.config(state="disabled")
        button_b.config(state="disabled")

# --- Widgets ---

label_logo = tk.Label(root,bg='black', fg='white', text=logo, font=("Courier", 10), justify="left")
label_logo.pack()

label_score = tk.Label(root, bg='black', fg='white', text="Score: 0", font=("Arial", 14))
label_score.pack()

label_a = tk.Label(root, text="", bg='black', fg='white', wraplength=550, font=("Arial", 12), pady=10)
label_a.pack()

label_vs = tk.Label(root, bg='black', fg='white', text=vs, font=("Courier", 10))
label_vs.pack()

label_b = tk.Label(root, bg='black', fg='white', text="", wraplength=550, font=("Arial", 12), pady=10)
label_b.pack()

button_frame = tk.Frame(root, bg='black')
button_frame.pack(pady=10)

button_a = tk.Button(button_frame, bg='black', fg='white', text="Choose A", width=15, command=lambda: make_choice('A'))
button_a.grid(row=0, column=0, padx=10)

button_b = tk.Button(button_frame, bg='black', fg='white', text="Choose B", width=15, command=lambda: make_choice('B'))
button_b.grid(row=0, column=1, padx=10)

winner_label = tk.Label(root, bg='black', fg='white', text="", font=("Arial", 14))
winner_label.pack(pady=10)

# Start the game
display_new_choices()

root.mainloop()
