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

income = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}
is_on = True


def display_menu():
    """ Returns the available menu"""
    print("☕☕☕☕☕")
    counter = 0
    for item in MENU:
        counter += 1
        print(f"{counter}. {item}")
    print("☕☕☕☕☕ ")


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry,There is no {item} for making that coffee")
            return False
    return True


def coins_processing():
    print("please insert coins: quarters,dimes,nickles,pennies)\n")
    total = int(input("How many quarters :")) * 0.25
    total += int(input("How many dimes:")) * 0.1
    total += int(input("How many nickles ")) * 0.05
    total += int(input("how many pennies ")) * 0.01
    return total


def is_transaction_complete(money_received, drink_cost):
    if money_received > drink_cost:
        global income
        income += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is the changes {change}")
        return True
    else:
        print("Money is not enough")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"☕☕☕ Enjoy your {drink_name} ☕☕☕ ")


print("""
☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕
=========== Drink coffee for life =========
""")
print("""
Follow the instructions to use the coffee machine 
- Type <off> to turn it off
- Type report to see the usage report 
- Type menu to view the available coffee """)

while is_on:
    choice = input("what would you like ?espresso/latte/cappuccino\n")
    if choice == 'off':
        is_on = False
    elif choice == 'menu':
        print("Available coffee types :")
        display_menu()
    elif choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Total income $ {income}")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            """quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01"""
            payment = coins_processing()
            is_transaction_complete(payment, drink['cost'])
            make_coffee(choice, drink['ingredients'])
    else:
        print("Invalid choice.try again")
