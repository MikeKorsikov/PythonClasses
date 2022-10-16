# SOLID
# The Single-Responsibility Principle (SRP)

class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass


# The Open-Closed Principle (OCP)

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


# The Liskov Substitution Principle (LSP)


'''
If in a subclass, you redefine a function that is also present 
in the base class, the two functions ought to have the same behaviour. 
This, though, does not mean that they must be mandatorily equal, 
but that the user, should expect that the same type of result, given the same input. 
'''

# The Interface Segregation Principle (ISP)

from abc import ABC, abstractmethod


class Walker(ABC):
    @abstractmethod
    def walk() -> bool:
        return print("Can Walk")


class Swimmer(ABC):
    @abstractmethod
    def swim() -> bool:
        return print("Can Swim")


class Human(Walker, Swimmer):
    def walk():
        return print("Humans can walk")

    def swim():
        return print("Humans can swim")


class Whale(Swimmer):
    def swim():
        return print("Whales can swim")


if __name__ == "__main__":
    Human.walk()
    Human.swim()

    Whale.swim()
    Whale.walk()

# The Dependency inversion Principle (DIP)

'''
principle is realised in API
'''