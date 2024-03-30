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
☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕
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

# TODO : 1  generate the report
# TODO : 2 track the repources
        
"""MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def display_menu():
#   Print the available menu and returns user needed coffee
  print("The coffee items available:\n")
  counter =0
  for item in MENU:
    counter +=1
    print(f"{counter}. {item}")
  print("\n")
  coffee = input("What would you like? (espresso/latte/cappuccino):")
  print(f"You would like to take {coffee}")
  if coffee not in MENU:
    print("That coffee is not available for now. check menu again")
  else:
    return coffee

def turn_off():
  turn = input("Type 'off' to turn off machine: ").lower()
  if turn == "off":
    return True
  else:
    return False

def check_resources(coffee):
#   Check if there is enough resources to make the coffee . return true otherwise false
  for item in MENU[coffee]["ingredients"]:
    if MENU[coffee]["ingredients"][item] > resources[item]:
      print(f"Sorry there is not enough {item}")
      return False
    else:
      return True
      

def process_coins():
#   Process the coins and return the total amount
  print("Please insert coins")
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickles?: "))
  pennies = int(input("How many pennies?: "))
  total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
  return total
    

def check_transaction(coffee, total):
#   Check if the transaction is successful. return true otherwise false
  if total < MENU[coffee]["cost"]:
    print("Sorry that's not enough money. Money refunded.")
    return False
  else:
    change = round(total - MENU[coffee]["cost"], 2)
    print(f"Here is ${change} in change.")
    return True

def make_coffee(coffee):
#   Make the coffee and deduct the resources
  for item in MENU[coffee]["ingredients"]:
    resources[item] -= MENU[coffee]["ingredients"][item]
  print(f"Here is your {coffee}. Enjoy!")

coffee =display_menu()
check_resources(coffee)
total = process_coins()
check_transaction(coffee, total)
make_coffee(coffee)

"""