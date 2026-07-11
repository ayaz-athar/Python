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
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_language(self):
        print(f"Programming language: {self.language}")


class Manager(Programmer):
    def __init__(self, name, salary, language, department):
        super().__init__(name, salary, language)
        self.department = department

    def show_department(self):
        print(f"Department: {self.department}")


manager = Manager("John", 80000, "Python", "IT")
manager.show_details()
manager.show_language()
manager.show_department()
