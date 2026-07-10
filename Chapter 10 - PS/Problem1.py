class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
        self.pin= 1234

p= Programmer("Ayaz", "Python")
print(p.name,p.product, p.pin, p.company)