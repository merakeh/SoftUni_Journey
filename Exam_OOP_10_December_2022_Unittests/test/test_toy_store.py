from Exam_OOP_10_December_2022_Unittests.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_correct_initializing(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_add_toy_to_non_existing_shelf_raise_exception(self):
        self.store.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
        }

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("D", "Mickey Mouse")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_that_already_exists_on_shelf_raise_exception(self):
        self.store.toy_shelf = {
            "A": "Mickey Mouse",
            "B": "Peppa Pig",
            "C": "Paw Patrol",
        }

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("B", "Peppa Pig")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_on_full_shelf_raise_exception(self):
        self.store.toy_shelf = {
            "A": "Mickey Mouse",
            "B": "Peppa Pig",
            "C": "Paw Patrol",
        }

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("B", "Teddy bear")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully(self):
        self.store.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
        }

        result = self.store.add_toy("A", "Mickey Mouse")
        self.assertEqual({
            "A": "Mickey Mouse",
            "B": None,
            "C": None,
        }, self.store.toy_shelf)

        self.assertEqual("Toy:Mickey Mouse placed successfully!", result)

    def test_remove_toy_from_non_existing_shelf_raise_exception(self):
        self.store.toy_shelf = {}

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Mickey Mouse")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_that_is_not_on_the_shelf_raise_exception(self):
        self.store.toy_shelf = {
            "A": "Mickey Mouse",
            "B": "Peppa Pig",
            "C": "Paw Patrol",
        }

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Peppa Pig")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_from_shelf_successfully(self):
        self.store.toy_shelf = {
            "A": "Mickey Mouse",
            "B": "Peppa Pig",
            "C": "Paw Patrol",
        }

        result = self.store.remove_toy("C", "Paw Patrol")
        self.assertEqual("Remove toy:Paw Patrol successfully!", result)
        self.assertEqual({
            "A": "Mickey Mouse",
            "B": "Peppa Pig",
            "C": None,
        }, self.store.toy_shelf)


if __name__ == "__main__":
    unittest.main()