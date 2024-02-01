from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

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
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("Input is not a valid drink order")