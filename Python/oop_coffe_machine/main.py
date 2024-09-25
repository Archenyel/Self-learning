from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffe_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

status = True



while status:

    options = my_menu.get_items()

    choice = input(f"what would you like?  ({options}):").lower()

    if(my_coffe_maker.is_resource_sufficient(my_menu.find_drink(choice)) == False) : continue

    match choice:
        case "espresso":
            print(" you have ordered an expresso ")
        case "latte":
            print(" ")
        case "cappuccino":
            print(" ")
        case "report":
            my_coffe_maker.report()
            my_money_machine.report()

        case "off" :
            status = False

print('the machine is off, good bye')



