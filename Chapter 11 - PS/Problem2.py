class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):
    def bark(self):
        print("Woof! Woof!")


d = Dog()
d.bark()