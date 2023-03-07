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