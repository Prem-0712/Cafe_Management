# Greet / INTRO
print("Welcome to PYTHON RESTAURANT !!")

# Defining Menu by using Dictionary 
menu = {
    "Pizza": 100,
    "Pasta": 70,
    "Shake": 50,
    "Burger": 100,
    "Coffee": 70
}

# Printing Menu for user
print("Pizza: 100")
print("Pasta: 70")
print("Shake: 50")
print("Burger: 100")
print("Coffee: 70")

# Defining the initial Total order price
total_price = 0

# Getting first item from the user by taking input
item_1 = str(input("What would uh like to order first ?: "))

if item_1 in menu:
    total_price += menu[item_1]

else:
    print("We are so sorry that, It's not avaliable yet.")
    print("But you can order something from the menu !")

another_order = str(input("Anything else you want to order: (yes/no)"))

if another_order == "yes":
    
    item_2 = str(input("What would you like to have ? "))

    if item_2 in menu:
        total_price += menu[item_2]

    else:
        print("Sorry it's not avaliable right now.")

print(f"Thank you for your order, your total bill is ₹{total_price}")