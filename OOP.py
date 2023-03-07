#zadanie 1
class Variables:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def print_vars(self):
        print(f"Variable 1: {self.var1}")
        print(f"Variable 2: {self.var2}")

    def change_vars(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def sum_vars(self):
        return self.var1 + self.var2

    def max_var(self):
        return max(self.var1, self.var2)

var = Variables(4,5)
var.change_vars(6,7)
print(var.sum_vars())
print(var.max_var())

#zadanie 2
class Counter:
    def __init__(self, start=0, end=10):
        self.start = start
        self.end = end
        self.value = start

    def increment(self):
        if self.value < self.end:
            self.value += 1
        else:
            self.value = self.start

    def decrement(self):
        if self.value > self.start:
            self.value -= 1
        else:
            self.value = self.end

    def get_value(self):
        return self.value

counter = Counter(3, 7)
print(counter.get_value())
counter.increment()
print(counter.get_value())
counter.decrement()
print(counter.get_value())
counter.decrement()
print(counter.get_value())

#zadanie 3
class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price, quantity):
        if name in self.products:
            self.products[name]['quantity'] += quantity
        else:
            self.products[name] = {'price': price, 'quantity': quantity}

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]

    def search_product(self, name):
        if name in self.products:
            return self.products[name]
        else:
            return f"{name} are absent"

shop = Shop()

shop.add_product('apple', 1.5, 10)
shop.add_product('banana', 2, 15)

print(shop.search_product('apple'))

shop.add_product('apple', 1.5, 5)
print(shop.search_product('apple'))

shop.remove_product('banana')
print(shop.search_product('banana'))

#zadanie 4
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        self.coins += v
        print(f'In MoneyBox {self.coins} coins')

box = MoneyBox(10)
print(box.can_add(5))
box.add(5)
print(box.can_add(3))
box.add(3)
print(box.can_add(7))

#zadanie 5

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
