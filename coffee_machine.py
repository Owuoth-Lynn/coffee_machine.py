""" Coffee maker application"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calculate():
    """ calculates coin value and returns a dollar value"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickels = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    return quarters + dimes + nickels + pennies


def is_resource_sufficient(order_ingredients):
    """ Returns True when order can be made and False when it cannot be made"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_the_cash_enough(cash_received, drink_cost):
    """ Returns True if payment is accepted and False if payment does not meet cost of drink"""
    if cash_received >= drink_cost:
        balance = round(cash_received - drink_cost, 2)
        print(f"Here is ${balance} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money")
        global profit
        profit += cash_received
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕️enjoy!")


is_on = True

# TODO: Ask the user to choose a type of coffee and get from dict resources needed
while is_on:
    user_choice = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        # TODO: Check if the resources available meet the demand and track use
        if is_resource_sufficient(drink["ingredients"]):
            user_cash = calculate()
            # TODO: Check if user inserted enough money and give change if user gives more than required
            if is_the_cash_enough(user_cash, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
