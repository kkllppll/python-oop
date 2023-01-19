import random
import datetime

class Menu():
    def __init__(self, menu_items):
        if menu_items: self.menu = menu_items
        else: self.menu = []

    def pizza_today(self):
        return random.choice(self.menu)

class Items():
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        

x = datetime.datetime.now()

Cheese = Items("Cheese", 110, 150)
Pepperoni = Items("Pepperoni", 100, 250)
Mushrooms = Items("Mushrooms", 500, 450)
Light = Items("Light", 220, 300)
Meat = Items("With Meat", 350, 500)
Margherita = Items("Margherita", 99, 120)
Hawaiian = Items("Hawaiian", 125, 350)
Chicken = Items("Chicken", 123, 340)

menu = Menu([Cheese, Pepperoni, Mushrooms, Light, Meat, Margherita, Hawaiian, Chicken])
pizza_today = menu.pizza_today()

print(f"It is", x.strftime("%A"), "!!!!")
print(f"Welcome to OURRR Pizzeria!!\nToday`s pizza of the day is: {pizza_today.name}!! - Price: {pizza_today.price} UAH for {pizza_today.weight} gram")
number = input("Would you like to see the whole menu — 1 or to buy the pizza of the day — 2?\nIf if you have already decided press the number.\nYour choice -> ")
if number == "1":
    print("Here is the menu. We have these types of pizzas:")
    for i in menu.menu: print(f"\n{i.name}. {i.price} UAH. {i.weight} gram.")

    pizza_name = input("\nEnter the name of the pizza you want to buy: ")
    for i in menu.menu:
            if pizza_name.lower() == i.name.lower():
                print(f"\nYour total is {i.price} UAH. Thanks for your choice! We will be happy to see you here again!")
                break
            else:
                continue
    else:
            print(f"Sorry we couldn`t find your pizza in your menu. Maybe we will have it later.\nTry our pizza of the day {pizza_today.name} {pizza_today.price} UAH. Thank you!")
            num = input("To try - 1, decline - 2\nYour choice ->")
            if num == "1":
                print(f"Your total is {pizza_today.price} UAH. Thank you! We will be happy to see you here again!")
            else: print("Bye! We will be happy to see you here again!")
                   
elif number == "2":
        print(f"Your total is {pizza_today.price} UAH. Thank you! We will be happy to see you here again!")
else:
        print("Error! Check your choice and try again!")



