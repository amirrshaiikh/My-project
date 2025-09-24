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
list1=[rock, paper, scissors]

choice1=int(input("What do you choose? Type 0 for Rock,"
                  " 1 for paper and 2 for scissors."))
choice2=random.randint(0,2)
print("You chose")
print(list1[choice1])
print("Computer chose")
print(list1[choice2])

if choice1==choice2:
    print("Draw")
elif ((choice1==0 and choice2==2) or
      (choice1==1 and choice2==0) or
      (choice1==2 and choice2==1)):
    print("You won")
else:
    print("Computer won")