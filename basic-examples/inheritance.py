from oopPython import Drink


class Beer(Drink):
    alcoholicGrade = "3.8%"  # static attributes

    def __init__(self, name, brand, price, quantity) -> None:
        super().__init__(name, brand)
        self.price = price
        self.quantity = quantity

    def details(self):
        return "The price of %s is %i and they are %s" % (self.name, self.price, self.quantity)

    def showBrand(self):  # Override method.
        return "The most luxury brand in the world!"

    @staticmethod
    def showClassInfo():
        return "This is a static method of the Beer class!"


dark = Beer("Dark", "Apple", 150, 10)
description = dark.description("The best beer in the world!")

print(description)
print(dark.showBrand())
print(dark.details())

print(Beer.alcoholicGrade)  # print a static attribute of the class
print(Beer.showClassInfo())  # print a static method of the class
