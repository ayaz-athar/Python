class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Salary: {self.salary}")


class Programmer(Employee):
    company = "ITC Infotech"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_details(self):
        super().show_details()
        print(f"Language: {self.language}")


programmer = Programmer("John", 80000, "Python")
programmer.show_details()
