class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")


harry = Employee("Harry", 30, "Developer")
#harry.language = "JavaScript" # This is an instance attribute
harry.getInfo()
harry.greet()
#employee.greet() # This will raise an error because greet is not a static method
