from Exam_OOP_10_December_2022.booths.open_booth import OpenBooth
from Exam_OOP_10_December_2022.booths.private_booth import PrivateBooth


class BoothCreator:

    booth_types = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def create_booth(self, type_booth: str, booth_number: int, capacity: int):
        return self.__class__.booth_types[type_booth](booth_number, capacity)
