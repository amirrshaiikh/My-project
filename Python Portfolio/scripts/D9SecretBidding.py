logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
more_bids=True
bidding={}
while more_bids:
    # TODO-1: Ask the user for input
    name=input("What is your name?")
    price=int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bidding[name]=price
    # TODO-3: Whether if new bids need to be added
    choice=input("Are there any other bidders? Type 'yes' or 'no'.")
    if choice=='no':
        more_bids=False
    else:
        print("\n" *20)
    # TODO-4: Compare bids in dictionary
winner=''
highest=0
for i in bidding:
    if highest < bidding[i]:
        highest=bidding[i]
        winner=i
print(f"The winner is {winner} with a bid of ${highest}")
