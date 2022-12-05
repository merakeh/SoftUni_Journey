import unittest

from mammal.project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("SomeName", "dog", "woof")

    def test_correct_initializing(self):
        self.assertEqual("SomeName", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("woof", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_make_sound_is_valid(self):
        result = self.mammal.make_sound()
        expected_result = f"SomeName makes woof"
        self.assertEqual(expected_result, result)

    def test_correct_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_if_info_returns_correct_message(self):
        result = self.mammal.info()
        self.assertEqual(f"SomeName is of type dog", result)


if __name__ == "__main__":
    unittest.main()

