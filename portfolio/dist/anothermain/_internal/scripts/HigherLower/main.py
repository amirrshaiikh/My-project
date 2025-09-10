from game_data import data
from art import *
import random

def compare(answer):
    if answer['A']['follower_count']> answer['B']['follower_count']:
        return 'A'
    else:
        return 'B'


while_condition=True
chosen_comp={}
chosen_dict= random.choice(data)
print(logo)
score=0
while while_condition:
    chosen_comp= random.choice(data)
    answers={ 'A': chosen_dict, 'B': chosen_comp}
    winner=answers[compare(answers)]
    print(f"Compare A: {chosen_dict['name']}, {chosen_dict['description']}, from {chosen_dict['country']}" )
    print(vs)
    print(f"Compare B: {chosen_comp['name']}, {chosen_comp['description']}, from {chosen_comp['country']}")
    choice=input("Who has more followers? Type 'A' or 'B'?").upper()
    if choice==compare(answers):
        score+=1
        print(f"You're right! Current score: {score}")
        chosen_dict=chosen_comp
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        while_condition=False
