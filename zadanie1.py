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
