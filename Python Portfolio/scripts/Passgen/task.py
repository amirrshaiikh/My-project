import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
def passgen():
    nr_letters=random.randint(4, 8)
    nr_symbols=random.randint(2, 4)
    nr_numbers=random.randint(3, 6)

    passw=''
    for let in range(nr_letters):
        passw+= letters[random.randint(0, 51)]
    for sym in range(nr_symbols):
        passw+=symbols[random.randint(0, 8)]
    for num in range(nr_numbers):
        passw+=numbers[random.randint(0,9)]
    #print(passw)
    lpassw=list(passw)
    # print(lpassw)
    random.shuffle(lpassw)
    # print(lpassw)
    final_password=''
    for i in lpassw:
        final_password+=i
    return final_password
    # print(final_password)