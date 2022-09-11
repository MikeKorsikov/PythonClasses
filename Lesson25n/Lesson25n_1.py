# Protocols and interfaces
from typing import Protocol, List, runtime_checkable


# protocol to be used by both classes
@runtime_checkable
class Item(Protocol):
    price: float
    discount: int


# first class
class Book:
    def __init__(self, title, author, price, discount):
        self.title = title
        self.author = author
        self.price = price
        self.discount = discount


# second class
class Product:
    def __init__(self, name, price, disc, producer):
        self.name = name
        self.price = price
        self.disc = disc  # still discount attribute but different wording
        self.producer = producer


# function to be used with both classes
def calculateTotalPrice(objs: List[Item]):
    sum = 0
    for obj in objs:
        if isinstance(obj, Item):
            sum += obj.price * (1 - obj.discount / 100)
        else:
            print("Error message: Incompatible type, review attribute names. (M)")
    return sum


# creating objects
book1 = Book("Python Crash Course", "Eric Matthes", 150, 25)
book2 = Book("JavaScript: The Good Parts", "Douglas Crockford", 178, 30)

# calling function
print('\n1) Calling function for several or one objects:')
print(calculateTotalPrice([book1, book2]))  # 237.1
print(calculateTotalPrice([book1]))  # 112.5

# alternatively
print('\n2) Alternative expression:')
purchase1 = calculateTotalPrice([
    Book("JavaScript: The Good Parts", "Douglas Crockford", 178, 30),
    Book("Python Crash Course", "Eric Matthes", 150, 25)
])
print(purchase1)  # 237.1

# combining objects from different classes
print('\n3) Combining several classes in one function:')
purchase3 = calculateTotalPrice([
    Book("JavaScript: The Good Parts", "Douglas Crockford", 178, 30),
    Product('Tea', 100, 15, 'Lipton'),
    Book("Python Crash Course", "Eric Matthes", 150, 25)
])
print(purchase3)  # 237.1
