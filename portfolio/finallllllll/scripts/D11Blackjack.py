import random



logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""





def deal_cards():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if len(cards)==2:
        if sum(cards)==21:
            return 0
    if 11 in cards:
        if sum(cards)>21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)


def comps_chance(c_cards):
    while calculate_score(c_cards)!=0 and calculate_score(c_cards)<17:
        c_cards.append(deal_cards())


def compare(u_total, c_total):
    if u_total==c_total:
        print("Draw")
    elif c_total==0:
        print("You lose, opponent got a blackjack")
    elif u_total==0:
        print("You win with a blackjack")
    elif u_total>21:
        print("You lose, you went over")
    elif c_total>21:
        print("YOu win, opponent went over")
    else:
        if c_total>u_total:
            print("You lose")
        else:
            print("You win")


def play_again():
    while_condition = True
    user_cards = []
    comp_cards = []
    for i in range(0, 2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())
    user_total = calculate_score(user_cards)
    comp_total = calculate_score(comp_cards)
    print(logo)
    while while_condition:
        print(f"Your cards: {user_cards} current score: {user_total}")
        print(f"Computer's first card: {comp_cards[0]}")
        user_total = calculate_score(user_cards)
        comp_total = calculate_score(comp_cards)
        if user_total == 0 or user_total > 21 or comp_total == 0:
            while_condition = False
        else:
            choice1 = input("Type 'y' to get another card, 'n' to pass: ")
            if choice1 == 'y':
                user_cards.append(deal_cards())
                user_total = calculate_score(user_cards)
            else:
                while_condition = False

    comps_chance(comp_cards)
    comp_total = calculate_score(comp_cards)
    compare(user_total, comp_total)
    print(f"Computer's cards {comp_cards} and score: {comp_total}")
    print(f"Your cards: {user_cards} current score: {user_total}")
    while input("Play again? 'y' to yes, 'n' to no")=='y':
        print("\n" *20)
        play_again()



choice = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if choice == 'n':
    exit()
else:
    play_again()