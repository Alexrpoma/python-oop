class Drink:
    def __init__(self, name, brand) -> None:
        self.name = name
        self.__brand = brand  #with __ the parameter is private -> __brand is private.
    def description(self, text) -> str:
        return "The " + self.name + " is " + text
    def showBrand(self):
        return "The brand is " + self.__brand

drink = Drink("water", "pepsi")
description = drink.description("is the most popular drink!")

print(description)
print(drink.showBrand())