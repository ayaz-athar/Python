class Employee:
    languafe = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

    def greet():
        print("Hello, welcome to the company!")


harry = Employee()
#harry.language = "JavaScript" # This is an instance attribute
harry.getInfo()
harry.greet()
#employee.greet() # This will raise an error because greet is not a static method