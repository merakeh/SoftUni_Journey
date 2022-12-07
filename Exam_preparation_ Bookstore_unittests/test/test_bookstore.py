from project.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):

    def setUp(self):
        self.store = Bookstore(15)
        self.books = {
            "The Notebook": 8,
            "Calculus for dummies": 5,
        }

    def test_correct_initializing(self):
        self.assertEqual(15, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_invalid_book_limit_set_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

    def test_correct__len__method(self):
        self.store.availability_in_store_by_book_titles = self.books
        self.assertEqual(13, len(self.store))

    def test_not_enough_space_to_receive_book_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Python Exercises", 3)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_add_new_book_correct(self):
        result = self.store.receive_book("New Book", 2)

        self.assertEqual(f"2 copies of New Book are available in the bookstore.", result)
        self.assertEqual({"New Book": 2}, self.store.availability_in_store_by_book_titles)

    def test_add_existing_book_correct(self):
        self.store.availability_in_store_by_book_titles = self.books

        result = self.store.receive_book("The Notebook", 1)
        self.assertEqual(f"9 copies of The Notebook are available in the bookstore.", result)

    def test_sell_book_that_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("New Book", 2)

        self.assertEqual(f"Book New Book doesn't exist!", str(ex.exception))

    def test_sell_more_copies_than_available_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("The Notebook", 10)

        self.assertEqual(f"The Notebook has not enough copies to sell. Left: 8", str(ex.exception))

    def test_sell_book_successfully(self):
        self.store.availability_in_store_by_book_titles = self.books
        result = self.store.sell_book("The Notebook", 3)

        self.assertEqual(f"Sold 3 copies of The Notebook", result)
        self.assertEqual(3, self.store.total_sold_books)
        self.assertEqual({
            "The Notebook": 5,
            "Calculus for dummies": 5,
        }, self.store.availability_in_store_by_book_titles)

    def test_correct__str__method(self):
        self.store.availability_in_store_by_book_titles = self.books

        expected_result = "Total sold books: 0\n" \
                          "Current availability: 13\n" \
                          " - The Notebook: 8 copies\n" \
                          " - Calculus for dummies: 5 copies"

        self.assertEqual(expected_result, str(self.store))



if __name__ == "__main__":
    unittest.main()