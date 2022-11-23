from encapsulation.pizza_maker.project.dough import Dough
from encapsulation.pizza_maker.project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, topping_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = topping_capacity
        self.toppings = dict()

    # setter for name parameter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    # setter for dough parameter
    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    # setter for topping_capacity parameter
    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    # methods
    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        return sum(self.toppings.values(), self.dough.weight)
