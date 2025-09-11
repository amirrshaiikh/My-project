from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
coffemaker=CoffeeMaker()
money=MoneyMachine()
cont=False
while True:
    choice=input(f"What would you like? ({menu.get_items()}): ")

    if choice=='off':
        exit(0)
    elif choice=='report':
        coffemaker.report()
        money.report()
    else:
        name=menu.find_drink(choice)
        cont=coffemaker.is_resource_sufficient(name) and money.make_payment(name.cost)
        if cont:
            coffemaker.make_coffee(name)