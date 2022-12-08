from exam_preparation_movie_unittests.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.movie = Movie("Movie1", 2000, 8.5)
        self.other = Movie("Movie2", 2005, 8.3)

    def test_correct_initializing(self):
        self.assertEqual("Movie1", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(8.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_setting_correct_name(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_setting_incorrect_year_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1500

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_adding_existing_actor_to_list(self):
        self.movie.actors = ["Pesho", "Gosho"]
        self.assertEqual("Pesho is already added in the list of actors!", self.movie.add_actor("Pesho"))

    def test_add_actor_non_existent_in_list(self):
        self.movie.add_actor("Pesho")
        self.assertEqual(["Pesho"], self.movie.actors)

    def test__gt__method_when_rating_is_greater_than_other(self):
        result = self.movie.__gt__(self.other)
        expected = '"Movie1" is better than "Movie2"'
        self.assertEqual(expected, result)

    def test__gt__method_when_rating_is_less_than_other(self):
        self.movie.rating = 8.0
        result = self.movie.__gt__(self.other)
        expected = '"Movie2" is better than "Movie1"'
        self.assertEqual(expected, result)

    def test__repr__method(self):
        self.movie.actors = ["Pesho", "Gosho"]
        expected = "Name: Movie1\n" \
                   "Year of Release: 2000\n" \
                   "Rating: 8.50\n" \
                   "Cast: Pesho, Gosho"

        self.assertEqual(expected, self.movie.__repr__())

if __name__ == "__main__":
    unittest.main()
