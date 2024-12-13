import random
import time
from rich import print

running = True
money = 0
menu = ("Pizza", "Hamburger", "Sandwich")
prices = {"Pizza": 10, "Hamburger": 7, "Sandwich": 5}

class Customer:
    def __init__(self) -> None:
        self.patience = random.randint(20, 60)
        self.order = random.choice(menu)
        self.start_time = time.time()
    
    def get_order(self):
        return self.order
    
    def get_patience(self):
        return self.patience
    
    def get_payment(self):
        base_price = prices[self.order]
        
        if time.time() - self.start_time > self.patience:
            return base_price - 3
        else:
            return base_price

print("Press Q to quit.")

while running:
    current_customer = Customer()
    print("The customer's order is [bold]" + current_customer.get_order() + "[/bold].")

    for item in menu:
        print(item)

    food = input("What will you serve the customer? ")
    
    if food == "q":
        running = False

    if not food.title() in menu:
        print("That food is unavailable!")

    
    if food.lower() == current_customer.get_order().lower():
        print("The customer's patience was " + str(current_customer.get_patience()) + ".")
        print("Earned [blue]$" + str(current_customer.get_payment()) + "[/blue].")
        money = money + current_customer.get_payment()
        print("Current Balance: [blue]$" + str(money) + "[/blue].")
    else:
        print("Final balance: [green]$" + str(money) + "[/green].")
        print("You lose.")
        running = False