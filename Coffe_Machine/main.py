from list import MENU
from list import resources

money = 0


def user_input():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    return order


def print_report():
    print(f"Current amount of resources in the machine:\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}")


def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


def coins():
    print("Please insert coins:")
    quarters = int(input("Quarter: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickes: "))
    pennies = int(input("Pennies: "))
    coins_inserted = (0.25*quarters) + (0.10*dimes) + (0.05*nickles) + (0.01*pennies)
    print(f"You have inserted ${coins_inserted}.")
    return coins_inserted


def transaction(coins, drink):
    if coins < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coins >= MENU[drink]["cost"]:
        change = coins - MENU[drink]["cost"]
        print(f"Here is ${change} in change.")
        global money
        money += MENU[drink]["cost"]
        return True


def brew(order):
    resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
    print(f"Here is your {order}. Enjoy!")


def coffee_machine():
    serve = True
    while serve == True:
        drink = user_input()
        if drink == "off":
            serve = False
        elif drink == "report":
            print_report()
            print(f"MONEY: ${money}")
        else:
            sufficient = check_resources(drink)
            if sufficient == True:
                money_inserted = coins()
                enough_money = transaction(money_inserted, drink)
                if enough_money == True:
                    brew(drink)


coffee_machine()