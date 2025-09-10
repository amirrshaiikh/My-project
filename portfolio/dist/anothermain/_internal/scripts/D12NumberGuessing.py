import random


logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""


print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100.")
difficulty=input("Choose difficulty. Type 'easy' or 'hard': ")
number_chosen=random.randint(1, 100)
if difficulty=='easy':
    attempt=10
else:
    attempt=5

while attempt>0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    attempt-=1
    if guess==number_chosen:
        print(f"You got it! The answer was {guess}")
        break
    elif guess> number_chosen:
        print("Too high")
    elif guess< number_chosen:
        print("Too low")
if attempt==0:
    print("You have run out of guesses. Refresh to play again")
