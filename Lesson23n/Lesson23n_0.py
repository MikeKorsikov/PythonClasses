# classes part-3 (starting page 65)

# Example 1
class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, b, a):
        super().__init__(a)
        self.b = b


class C(A):
    def __init__(self, c, a):
        super().__init__(a)
        self.c = c


class D(B, C):
    def __init__(self, d, a, b):
        super().__init__(b, a)
        self.d = d


# print(D.mro())

# Example 2
class A1:
    def __init__(self, a):
        self.a = a

    def show(self):
        print(f'Value: {self.a}')


class B1(A1):
    def __init__(self, b, a):
        super().__init__(a)
        self.b = b

    def show(self):
        super().show()
        print(f'B value: {self.b}')

# # calling methods
# a = A1(1)
# a.show()
#
# b = B1(2, 1)
# b.show()


# Example 3 (magic methods) todo read about magic methods
class Digit:
    def __new__(cls, *args, **kwargs):
        print('__new__ call')
        return object.__new__(cls)

    def __init__(self, num):
        print('__init__ call')
        self.num = num


# create objects
# d1 = Digit(1)

class Distance:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __add__(self, other):
        temp = Distance()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp

    def __eq__(self, other):
        result = self.x == other.x and self.y == other.y
        return result

    def __neg__(self, other):
        return not Distance.__eq__(self, other)

    def __le__(self, other):
        result = self.x <= other.x and self.y <= other.y
        return result

    def __str__(self):
        return f'x: {self.x} y: {self.y}'


# testing
d1 = Distance(5, 5)
d2 = Distance(5, 5)

print(d1 <= d2)

# get items
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def __getitem__(self, key):
        return self.__marks.get(key)

s1 = Student('alex', {'math':4, 'eng': 4, 'sport': 10})
print(s1['math'])

#
class Team:
    def __init__(self, teacher, logbooks):
        self.teacher = teacher
        self.__logbooks = logbooks

    def __getitem__(self, key):
        x1, x2 = key
        return self.__logbooks.get(x1).get(x2)

t1 = Team('John', {'alex': {'math': 5, 'eng': 4},
                   'den': {'math':3, 'eng': 2}})

print(t1['den', 'eng'])