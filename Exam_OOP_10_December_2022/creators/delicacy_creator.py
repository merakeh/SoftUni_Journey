from Exam_OOP_10_December_2022.delicacies.gingerbread import Gingerbread
from Exam_OOP_10_December_2022.delicacies.stolen import Stolen


class DelicacyCreator:

    delicacy_types = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    def create_delicacy(self, type_delicacy: str, name: str, price: float):
        return self.__class__.delicacy_types[type_delicacy](name, price)
