logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

operation_dictionary={
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
start_over=True
while start_over:
    # Instead of using 2 while loops we can simply use recursive function
    continue_working=True
    print(logo)
    num1=int(input("What's the first number?: "))
    while continue_working:
        for symbol in operation_dictionary:
            print(symbol)
        op=input("Pick an operation: ")
        num2=int(input("What's the next number?: "))
        my_favorite_function = operation_dictionary[op]
        result=my_favorite_function(num1, num2)
        print(f"{num1} {op} {num2} = {result}")
        choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice=='n':
            continue_working=False
        else:
            num1=result