import unittest
from ecommerce import Product, OrderItem, Order, User

class TestECommerceSystem(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@mail.com")
        self.product1 = Product("Laptop", 1000.0, "Gaming Laptop")
        self.product2 = Product("Mouse", 50.0, "Wireless Mouse")
        self.order = Order()

    def test_user_registration(self):
        self.assertEqual(self.user.register(), "testuser зареєстровано!")

    def test_user_login(self):
        self.assertEqual(self.user.login(), "testuser увійшов у систему.")

    def test_add_product_to_order(self):
        self.order.add_product(self.product1, 1)
        self.assertEqual(len(self.order.items), 1)

    def test_remove_product_from_order(self):
        self.order.add_product(self.product1, 1)
        self.order.remove_product(self.product1)
        self.assertEqual(len(self.order.items), 0)

    def test_calculate_total(self):
        self.order.add_product(self.product1, 1)
        self.order.add_product(self.product2, 2)
        self.assertEqual(self.order.calculate_total(), 1000.0 + 2*50.0)

    def test_order_item_total_price(self):
        item = OrderItem(self.product1, 3)
        self.assertEqual(item.get_total_price(), 3000.0)

    def test_user_place_order(self):
        self.user.place_order(self.order)
        self.assertIn(self.order, self.user.view_orders())

    def test_order_contains_correct_items(self):
        self.order.add_product(self.product1, 2)
        self.assertEqual(self.order.items[0].quantity, 2)

    def test_product_attributes(self):
        self.assertEqual(self.product1.name, "Laptop")
        self.assertEqual(self.product1.price, 1000.0)

    def test_multiple_orders(self):
        order2 = Order()
        self.user.place_order(self.order)
        self.user.place_order(order2)
        self.assertEqual(len(self.user.orders), 2)

if __name__ == "__main__":
    unittest.main()
