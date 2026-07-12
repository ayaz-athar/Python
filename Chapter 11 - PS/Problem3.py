class Employee:
    salary = 50000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e = Employee()

print("Salary After Increment:", e.salaryAfterIncrement)

e.salaryAfterIncrement = 60000

print("New Increment:", e.increment)