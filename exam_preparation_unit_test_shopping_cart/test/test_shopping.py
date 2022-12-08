from exam_preparation_unit_test_shopping_cart.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Name", 100.0)
        self.other_cart = ShoppingCart("OtherCart", 200)

    def test_correct_initializing(self):
        self.assertEqual("Name", self.cart.shop_name)
        self.assertEqual(100.0, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_setting_incorrect_shop_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "name 2"

        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_product_with_too_high_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("Product1", 150)

        self.assertEqual(f"Product Product1 cost too much!", str(ve.exception))

    def test_add_product_to_cart_expect_correct(self):
        result = self.cart.add_to_cart("Product", 20)
        self.assertEqual({"Product": 20}, self.cart.products)
        self.assertEqual("Product product was successfully added to the cart!", result)

    def test_remove_non_existing_product_from_cart_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Product")

        self.assertEqual("No product with name Product in the cart!", str(ve.exception))

    def test_remove_existing_product_from_cart_expect_correct(self):
        self.cart.products = {"Product1": 2, "Product2": 1}
        result = self.cart.remove_from_cart("Product1")
        self.assertEqual({"Product2": 1}, self.cart.products)
        self.assertEqual("Product Product1 was successfully removed from the cart!", result)

    def test__add__method(self):
        self.cart.products = {"Product1": 2}
        self.other_cart.products = {"Product2": 1}
        new_shopping_cart = self.cart.__add__(self.other_cart)
        self.assertEqual("NameOtherCart", new_shopping_cart.shop_name)
        self.assertEqual(300.0, new_shopping_cart.budget)
        self.assertEqual({"Product1": 2, "Product2": 1}, new_shopping_cart.products)

    def test_try_buying_but_not_enough_budget_raises_value_error(self):
        self.cart.products = {"Product1": 20, "Product2": 100}
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        expected = "Not enough money to buy the products! Over budget with 20.00lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_buy_products_successfully(self):
        self.cart.products = {"Product1": 20, "Product2": 15}
        result = self.cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 35.00lv.", result)


if __name__ == "__main__":
    unittest.main()
