
class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def check_inventory(self, product, quantity):
        if product in self.products and self.products[product] >= quantity:
            return True
        else:
            return False

    def process_order(self, product, quantity):
        if self.check_inventory(product, quantity):
            self.products[product] -= quantity
            return True
        else:
            return False

    def request_product(self, product, quantity):
        print(f"Requesting more {product.name}...")



class ProductManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def add_product(self, product, quantity):
        self.inventory.add_product(product, quantity)


class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Customer:
    def __init__(self, inventory):
        self.inventory = inventory

    def place_order(self, order):
        if self.inventory.process_order(order.product, order.quantity):
            print("Order placed successfully!")
        else:
            print("Sorry, the product is out of stock. Requesting more...")
            self.inventory.request_product(order.product, order.quantity)


inventory = Inventory()
product_manager = ProductManager(inventory)
customer = Customer(inventory)

product = Product("Apple iPhone 13", "Phone", 999.99, 10)
product_manager.add_product(product, 10)

#order = Order(product, 11)
order = Order(product, 3)
customer.place_order(order)
