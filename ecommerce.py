class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


class Order:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append(OrderItem(product, quantity))

    def remove_product(self, product):
        self.items = [item for item in self.items if item.product != product]

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.orders = []

    def register(self):
        return f"{self.username} зареєстровано!"

    def login(self):
        return f"{self.username} увійшов у систему."

    def view_orders(self):
        return self.orders

    def place_order(self, order):
        self.orders.append(order)

