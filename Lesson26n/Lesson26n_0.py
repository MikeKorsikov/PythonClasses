# metaclass is a class creating other classes
from pprint import pprint

# example
print('\n1) Use of __new__ and __init__:')
class Number:
    def __new__(cls, *args, **kwargs):
        print(f"calling __new__ for {str(cls)} \t {super()} \t {super().__new__(cls)}")
        return super().__new__(cls)

    def __init__(self, num):
        print(f"calling __init__ for {str(self)}")
        self.num = num


# crete new class/object
n1 = Number(1)
print(type(n1))
print(type(Number))


# example
print('\n2) Example of metaclass:')
class Human(type):
    def __new__(mcs, name, bases, class_dict):
        class_ = super().__new__(mcs, name, bases, class_dict)
        class_.freedom = True
        return class_


class Person(object, metaclass=Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age


pprint(Person.__dict__)


# create new class using type
print('\n3) Creating classes using type:')
name = 'mykola1'
NewClass = type(f'{name}', (), {'num': None, 'my_method': lambda self: print('call my method')})


# create new class/object
nc1 =NewClass()
nc1.my_method()
print(nc1)


# singleton
print('\n4) Singleton:')
class Fild:  # descriptor
    def __set_name__(self, owner, name):  # owner is a class
        self.var = "__" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.var]

    def __set__(self, instance, value):
        instance.__dict__[self.var] = value


class Singleton:
    user = Fild()
    password = Fild()
    url = Fild()

    __instance = None

    # if we need to create only one object and not multiple unique objects
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, password, url):
        self.user = user
        self.password = password
        self.url = url

    def connect(self):
        print(f"Connecting to ... DB {self.url}")

    def close(self):
        print(f"Disconnecting from ... DB {self.url}")

    def read(self):
        print(f"Getting data from ... DB {self.url}")

    @staticmethod
    def write(self):
        print(f"Writing data to ... DB {self.url}")


# creating objects
s1 = Singleton('root', 'password1', 'MYSQL')
print(s1.user)
s1.connect()

s2 = Singleton('admin', 'password2', 'NoSQL')
print(s2.user)
s2.read()

# where __new__ section is introduced test is TRUE (objects are the same)
print(s1 == s2)


# Interface - class without any functionality
print('\n5) Interface and abstract methods:')
class Interface:
    name = ''
    age = ''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):  # abstract method is method without functionality
        pass


class Person (Interface):
    def __init__(self, name, age):
        super().__init__(name, age)


mykola = Person('Mykola', 29)
mykola.show()


# Protocol - to define implicit interfaces
print('\n6) Protocol:')
from typing import List, Protocol


class Item(Protocol):
    quantity: float
    price: float


class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


def calculate_total(items: List[Item]) -> float:
    return sum([item.quantity * item.price for item in items])


# calculate total a product list
total = calculate_total([
    Product('A', 10, 150),
    Product('B', 5, 250)
])

print(total)