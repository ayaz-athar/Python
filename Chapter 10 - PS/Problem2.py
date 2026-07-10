class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y != 0:
            self.result = x / y
        else:
            self.result = "Error: Division by zero is not allowed."

a= Calculator()
a.add(10, 5)
print(a.result)  # Output: 15
a.subtract(10, 5)
print(a.result)  # Output: 5
a.multiply(10, 5)
print(a.result)  # Output: 50
a.divide(10, 0)
print(a.result)  # Output: Error: Division by zero is not allowed.