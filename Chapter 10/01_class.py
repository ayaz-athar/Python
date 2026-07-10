class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")