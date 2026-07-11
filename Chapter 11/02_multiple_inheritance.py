class Employee:
    company = "ITC"
    name = "John"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()

