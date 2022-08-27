# class and static method

class Human:
    __id = 0

    def __init__(self, name):
        self.name = name

    @classmethod  # cls
    def foo(cls):
        print(f'Class hello {cls.__id}')

    @staticmethod
    def st():
        print(f'Static hello {Human.__id}')

    def get_name(self):
        return self.name


# create object
h1 = Human('Den')
h1.foo()
h1.st()
print(h1.get_name())

# inheritance in classes
print('\nInheritance in classes:')


class Animal:
    def __init__(self, name):
        self.name = name
        print('Object animal created.')

    def info(self):
        print(f"Animal's name is: {self.name}")


class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name)
        self.age = age
        self.owner = owner
        print('Object dog is created.')

    def info(self):
        print(f'Owner is: {self.owner}')


bullet = Dog('Patron', 2, 'ZSU')
print(f"Dog name: {bullet.name}")
bullet.info()
