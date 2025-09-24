import tkinter as tk
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list1 = [rock, paper, scissors]

def play(choice1):
    choice2 = random.randint(0, 2)

    result = ""

    if choice1 == choice2:
        result = "Draw"
    elif ((choice1 == 0 and choice2 == 2) or
          (choice1 == 1 and choice2 == 0) or
          (choice1 == 2 and choice2 == 1)):
        result = "You won"
    else:
        result = "Computer won"

    user_choice_label.config(text=f"You chose:\n{list1[choice1]}")
    computer_choice_label.config(text=f"Computer chose:\n{list1[choice2]}")
    result_label.config(text=result)

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Title Label
title_label = tk.Label(root, text="Choose Rock (0), Paper (1), or Scissors (2):", font=("Arial", 14))
title_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock (0)", command=lambda: play(0), width=15)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper (1)", command=lambda: play(1), width=15)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors (2)", command=lambda: play(2), width=15)
scissors_button.grid(row=0, column=2, padx=5)

# Labels to display choices and result
user_choice_label = tk.Label(root, text="", font=("Courier", 10), justify="left")
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="", font=("Courier", 10), justify="left")
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
