# classes part-2 (page 30)


class Person:
    __info = 'Person male caucasian'
    __count = 0
    __i = 0

    def __init__(self, name, age):
        self.__id = Person.__i
        self.age = age
        self.name = name
        Person.__count += 1
        Person.__i += 1
        print(f'Object ID {self.__id} was created')

    @staticmethod
    def get_info():
        print(Person.__info)

    @staticmethod
    # todo read about static methods...
    def set_info(value):
        Person.__info = value

    def info(self):
        print(f'ID: {self.__id}')

    def __del__(self):
        Person.__count -= 1
        print(f'Object ID {self.__id} was deleted.')


# create new object 1
print('Object1:')
p1 = Person('Sarah', 20)
print('before change:')
p1.get_info()

print('after change:')
p1.set_info('Female asian')
p1.get_info()
p1.info()

# create new object 2
print('\nObject2:')
p2 = Person('John', 30)
p2.get_info()
p2.info()

# comparing objects
print('\nObjects are the same?')
print(p1)
print(p2)
print(p1 == p2)

# deleting object
print('\nDeleting object:')
del p1

# create new object 3
print('\nObject 3:')
p3 = Person('Max', 50)
p3.info()
