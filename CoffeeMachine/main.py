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

def is_resource_sufficient(order_ingredients):
    """Returns true if the drink can be made"""
    for item in order_ingredients:
        if order_ingredients[item] >=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def process_coins():
    """returns the toal caluclated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def is_transactions_successful(money_received, drink_cost):
    """Return true when the payment is accepted, or False if the money is insufficient"""
    if (money_received >= drink_cost) :
        change = round(money_received - drink_cost, 2)
        print(f"Heres is ${change} amount in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the requird ingredients from resource list"""
    for item in order_ingredients:
        resources[item ] -= order_ingredients[item]
        print(f"Spending resource: {order_ingredients[item]} of {item}")
    print(f"Here is your {drink_name} ☕. Enjoy!")

is_on = True
while (is_on):
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        # dictionary with ingredients
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins() #check that inserted enough money for the drink, and give change if necessary
            if is_transactions_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
