# classes

# creating class (simple)
class Person:
    name = 'Default'
    age = 0


# accessing data
woman = Person()
woman.name = 'Lera'
woman.age = 29


# creating class (with constructor init)

class Dad:
    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        print(f"\nName: {self.first_name} "
              f"\nLast name: {self.last_name}"
              f"\nage: {self.age}")


# Creating object
son = Dad('Konan', 'Korsikov', 1)

# Calling function from object
son.info()


#  public vs private parameters and functions
print('\nPublic vs private parameters and functions:\n')
import random

class Dog:
    def __init__(self, name, dob, breed, age, owner):
        # public variables
        self.owner = owner
        self.age = age
        self.breed = breed
        self.dob = dob
        self.name = name

        # private variables
        self.__id = random.randint(0, 1000000)
        self.__code = "_"

    # public functions
    def info(self):
        print(f"ID: {self.__id}")
        for i, v in self.__dict__.items():
            print(i, v)

    def get_code(self):
        return self.__code

    def set_code(self, __code):
        self.__code = code

    # private function
    def __get_id(self):
        return self.__id


# create new object
d1 = Dog('Mars', '03.06.2021', 'German Shepard', '1', 'Alex')

# calling function from class to display object values
d1.info()

print("\nAll parameters of class:")
for i in d1.__dict__:
    print(i, end=", ")

# getting value
print('\nGetter:')
print(f"Value we GET is:{d1.get_code()}")

# setting value
print('\nSetter:')
d1.set_code ='!'
print(f"Value we SET is:{d1.set_code}")