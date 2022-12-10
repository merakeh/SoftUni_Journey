from Exam_OOP_10_December_2022.creators.booth_creator import BoothCreator
from Exam_OOP_10_December_2022.creators.delicacy_creator import DelicacyCreator


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

        self.delicacy_creator = DelicacyCreator()
        self.booth_creator = BoothCreator()

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if any(d.name == name for d in self.delicacies):
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.delicacy_creator.delicacy_types.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.delicacy_creator.create_delicacy(type_delicacy, name, price)

        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if any(b.booth_number == booth_number for b in self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.booth_creator.booth_types.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.booth_creator.create_booth(type_booth, booth_number, capacity)

        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if booth.is_reserved:
                continue
            if booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved" \
                       f" for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_booth_by_number(booth_number)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.find_delicacy(delicacy_name)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_booth_by_number(booth_number)

        bill = booth.price_for_reservation
        for order in booth.delicacy_orders:
            bill += order.price

        self.income += bill

        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def find_booth_by_number(self, booth_number):
        for b in self.booths:
            if b.booth_number == booth_number:
                return b
        return None

    def find_delicacy(self, delicacy_name):
        for d in self.delicacies:
            if d.name == delicacy_name:
                return d
        return None

