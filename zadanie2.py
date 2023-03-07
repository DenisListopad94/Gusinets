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
