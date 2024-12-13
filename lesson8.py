class Pizza:
    def __init__(self, sauce, crust):
        self.sauce = sauce
        self.crust = crust
    
    def get_sauce(self):
        return self.sauce
    
    def get_crust(self):
        return self.crust

class Pizza_With_Toppings(Pizza):
    def __init__(self, sauce, crust):
        super().__init__(sauce, crust)
        self.toppings = []
    
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def get_toppings(self):
        return self.toppings

simple_cheese_pizza = Pizza("tomato", "standard")

pepperoni_pizza = Pizza_With_Toppings("tomato", "standard")
pepperoni_pizza.add_topping("pepperoni")

print(type(simple_cheese_pizza))
print(simple_cheese_pizza.get_sauce())
print(simple_cheese_pizza.get_crust())

print(type(pepperoni_pizza))
print(pepperoni_pizza.get_sauce())
print(pepperoni_pizza.get_crust())
print(pepperoni_pizza.get_toppings())