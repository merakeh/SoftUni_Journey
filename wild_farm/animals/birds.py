from wild_farm.animals.animal import Bird
from wild_farm.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def gained_weight(self):
        return 0.35
