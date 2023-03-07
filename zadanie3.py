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
