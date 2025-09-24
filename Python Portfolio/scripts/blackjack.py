import tkinter as tk
import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Game logic functions (unchanged from your code)

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def comps_chance(c_cards):
    while calculate_score(c_cards) != 0 and calculate_score(c_cards) < 17:
        c_cards.append(deal_cards())

def compare(u_total, c_total):
    if u_total == c_total:
        return "Draw"
    elif c_total == 0:
        return "You lose, opponent got a Blackjack"
    elif u_total == 0:
        return "You win with a Blackjack"
    elif u_total > 21:
        return "You lose, you went over"
    elif c_total > 21:
        return "You win, opponent went over"
    elif c_total > u_total:
        return "You lose"
    else:
        return "You win"

# GUI setup

root = tk.Tk()
root.title("Blackjack Game")
root.config(bg='black')

# Game variables
user_cards = []
comp_cards = []
user_total = 0
comp_total = 0
game_over = False

# Widgets

logo_label = tk.Label(root, text=logo, font=("Courier", 7), justify="left", bg='black', fg='white')
logo_label.pack()

user_label = tk.Label(root, text="", font=("Arial", 12), bg='black', fg='white')
user_label.pack()

comp_label = tk.Label(root, text="", font=("Arial", 12), bg='black', fg='white')
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg='black', fg='white')
result_label.pack(pady=10)

def update_labels():
    user_total = calculate_score(user_cards)
    comp_display = f"{comp_cards[0]}, ?" if not game_over else ', '.join(map(str, comp_cards))
    comp_score = "" if not game_over else f"Score: {calculate_score(comp_cards)}"
    user_label.config(text=f"Your cards: {user_cards}  | Score: {user_total}")
    comp_label.config(text=f"Computer's cards: {comp_display}  {comp_score}")

def hit():
    global user_total, game_over
    if not game_over:
        user_cards.append(deal_cards())
        user_total = calculate_score(user_cards)
        update_labels()

        if user_total > 21 or user_total == 0:
            stand()

def stand():
    global game_over, comp_total
    game_over = True
    comps_chance(comp_cards)
    comp_total = calculate_score(comp_cards)
    user_total = calculate_score(user_cards)
    result = compare(user_total, comp_total)
    result_label.config(text=result)
    update_labels()
    hit_button.config(state="disabled")
    stand_button.config(state="disabled")

def reset_game():
    global user_cards, comp_cards, user_total, comp_total, game_over
    user_cards = [deal_cards(), deal_cards()]
    comp_cards = [deal_cards(), deal_cards()]
    user_total = calculate_score(user_cards)
    comp_total = calculate_score(comp_cards)
    game_over = False
    result_label.config(text="")
    update_labels()
    hit_button.config(state="normal")
    stand_button.config(state="normal")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)
button_frame.config(bg='black')

hit_button = tk.Button(button_frame, text="Hit", width=12, command=hit, bg='black', fg='white')
hit_button.grid(row=0, column=0, padx=5)

stand_button = tk.Button(button_frame, text="Stand", width=12, command=stand, bg='black', fg='white')
stand_button.grid(row=0, column=1, padx=5)

restart_button = tk.Button(root, text="Play Again", command=reset_game, bg='black', fg='white')
restart_button.pack(pady=10)

# Initial game start
reset_game()

root.mainloop()
