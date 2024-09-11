MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
        "cost": 3.5,
    }
}
machine_continue = True
money = 0
resource_values = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resource_values["water"]}")
    print(f"Milk: {resource_values["milk"]}")
    print(f"Coffee: {resource_values["coffee"]}")
    print(f"Money: ${money}")


def processing(user_prompt):
    if MENU[user_prompt]["ingredients"]["water"] > resource_values["water"]:
        print("Sorry there is not enough water.")
    elif MENU[user_prompt]["ingredients"]["milk"] > resource_values["milk"]:
        print("Sorry there is not enough milk.")
    elif MENU[user_prompt]["ingredients"]["coffee"] > resource_values["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        quarters = int(input("Quarters: "))
        dimes = int(input("Dimes: "))
        nickels = int(input("Nickels: "))
        pennies = int(input("Pennies: "))
        inserted_coins = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
        if inserted_coins < MENU[user_prompt]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            global money
            money += MENU[user_prompt]["cost"]
            change = inserted_coins - MENU[user_prompt]["cost"]
            print(f"Here is ${round(change, 2)} dollars in change.")
            resource_values["water"] -= MENU[user_prompt]["ingredients"]["water"]
            resource_values["milk"] -= MENU[user_prompt]["ingredients"]["milk"]
            resource_values["coffee"] -= MENU[user_prompt]["ingredients"]["coffee"]
            print(f"Here's your {user_prompt}, Enjoy!")


while machine_continue:
    prompt = input("What would you like? (espresso/ latte/ cappuccino):").lower()
    if prompt == "report":
        report()
    elif prompt == "espresso":
        processing(prompt)
    elif prompt == "latte":
        processing(prompt)
    elif prompt == "cappuccino":
        processing(prompt)
    elif prompt == "off":
        machine_continue = False
    else:
        print("Invalid Input. Machine turned off.")
        machine_continue = False
