from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#TODO 1. Print report -> DONE
#TODO 2. Check sufficient resources available

#TODO 3. Process coins
#TODO 4. Check if transaction was successful
#TODO 5. Make coffee

continue_to_order = True
while continue_to_order:
    drink_order = input("Which drink would you like? (espresso/latte/cappuccino): ").lower()
    if drink_order == "report":
        coffee_maker.report()
    elif drink_order == "off":
        continue_to_order = False
    elif drink_order == "espresso" or drink_order == "latte" or drink_order == "cappuccino":
        drink = menu.find_drink(drink_order)
        if coffee_maker.is_resource_sufficient(drink):
            print("RESOURCES AVAILABLE")
            
        else:
            print("RESOURCES NOT AVAILABLE")
    else:
        print("Input is not a valid drink order")