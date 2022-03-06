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

money = 0.0

resources = {
    "water": 1000,
    "milk": 750,
    "coffee": 500,
}


# Check Enough Ingredients.
def resources_sufficient(ingredients):
    """Retuens True when order can be made. False if ingredients are insufficient."""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Coins Processing.
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# Is Transaction Successfull.
def transaction_successfull(inserted_money, drink_cost):
    """Returns True when the payment is successfull or accepted, or False if not successfull."""
    if inserted_money >= drink_cost:
        change = round(inserted_money - drink_cost, 2)
        print(f"Here is your ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money Refunded.")
        return False


# Make Coffee
def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")



coffee_machine = True
while coffee_machine:
    
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino).
    user_choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        coffee_machine = False

    # TODO: 3. Print report.
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    else:
        drink = MENU[user_choice]
        
        # TODO: 4. Check resources sufficient?
        if resources_sufficient(drink["ingredients"]):

            # TODO: 5. Process coins.
            payment = process_coins()

            # TODO: 6. Check transaction successful?
            if transaction_successfull(payment, drink["cost"]):
                
                # TODO: 7. Make Coffee.
                make_coffee(user_choice, drink["ingredients"])