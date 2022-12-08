from exam_preparation_plantation_unittests.plantation import Plantation
import unittest


class TestPlantation(unittest.TestCase):

    def setUp(self):
        self.plantation = Plantation(5)

    def test_correct_initializing(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_set_incorrect_size_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_existing_worker_raise_value_error(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Pesho")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_successfully(self):
        result = self.plantation.hire_worker("Pesho")
        self.assertEqual("Pesho successfully hired.", result)
        self.assertEqual(["Pesho"], self.plantation.workers)

    def test__len__method(self):
        self.plantation.plants = {"Pesho": ["rose", "lilly", "tree"], "Gosho": ['lilly', 'rose']}
        self.assertEqual(5, self.plantation.__len__())

    def test_planting_but_worker_does_not_exist_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Pesho", "lilly")

        self.assertEqual("Worker with name Pesho is not hired!", str(ve.exception))

    def test_planting_but_plantation_is_full_raise_value_error(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"Pesho": ["rose", "rose", "rose", "rose", "rose"]}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Pesho", 'lilly')

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_not_for_the_first_time_expect_correct(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"Pesho": ['rose']}

        result = self.plantation.planting("Pesho", 'lilly')
        self.assertEqual("Pesho planted lilly.", result)
        self.assertEqual({"Pesho": ['rose', 'lilly']}, self.plantation.plants)

    def test_planting_for_first_time_worker_already_exists_expect_correct(self):
        self.plantation.workers = ["Pesho"]

        result = self.plantation.planting("Pesho", 'lilly')

        self.assertEqual("Pesho planted it's first lilly.", result)
        self.assertEqual({"Pesho": ['lilly']}, self.plantation.plants)

    def test__str__method(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        self.plantation.plants = {"Pesho": ['rose', "tree"], "Gosho": ['lilly']}

        expected = "Plantation size: 5\n" \
                   "Pesho, Gosho\n" \
                   "Pesho planted: rose, tree\n" \
                   "Gosho planted: lilly"

        self.assertEqual(expected, str(self.plantation))

    def test__repr__method(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        expected = "Size: 5\n" \
                   "Workers: Pesho, Gosho"

        self.assertEqual(expected, self.plantation.__repr__())


if __name__ == "__main__":
    unittest.main()










