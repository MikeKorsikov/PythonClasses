# static method
'''
class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    @staticmethod
    def printNumInstances():
        print(f"Number of instances created {Spam.numInstances}.")


# example
a = Spam()
b = Spam()
c = Spam()

Spam.printNumInstances()
a.printNumInstances()


# classmethod and staticmethod
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))


# user defined decorators
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)


@tracer
def spam(a, b, c):
    return a + b + c


print(spam(1, 2, 3))


# property
class Person: # Add (object) in 2.X
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")


bob = Person('Bob Smith') # bob has a managed attribute
print(bob.name) # Runs getName
bob.name = 'Robert Smith' # Runs setName
print(bob.name)
del bob.name # Runs delName

print('-'*20)
sue = Person('Sue Jones') # sue inherits property too
print(sue.name)
print(Person.name.__doc__) # Or help(Person.name)



# descriptor
class Descriptor:
    def __get__(self, instance, owner):
        print('Getter invoked')

    def __set__(self, instance, value):
        print('Setter invoked')

    def __delete__(self, instance):
        pass


class Subject:
    attr = Descriptor()


X = Subject()
X.attr = 1
print(X.attr)


# decorators - callable objects that process other callable objects
calls = 0


# function decorator as function
def tracer(func):  # State via enclosing scope and global
    def wrapper(*args, **kwargs):  # Instead of class attributes
        global calls  # calls is global, not per-function
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper


@tracer
def spam(a, b, c):  # Same as: spam = tracer(spam)
    print(a + b + c)


# example
spam(1, 2, 3)


# function decorator as class
class tracerAlt:
    def __init__(self, func):  # On @ decorator
        self.calls = 0  # Save func for later call
        self.func = func

    def __call__(self, *args, **kwargs):  # On call to original function
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracerAlt
def spam2(a, b, c):  # spam = tracer(spam)
    print(a + b + c)  # Triggers tracer.__init__


# example
spam2(1, 2, 3)  # Runs tracer.__call__


# function decorator to check time elapsed during function execution
import time, sys

force = list if sys.version_info[0] == 3 else (lambda X: X)


class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kargs):
        start = time.process_time()
        result = self.func(*args, **kargs)
        elapsed = time.process_time() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@timer
def listcomp(N):
    return [x * 2 for x in range(N)]


result = listcomp(500000)
'''


# Class decorator
def Tracer(aClass):  # On @ decorator
    class Wrapper:
        def __init__(self, *args, **kargs):  # On instance creation
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)  # Use enclosing scope name

        def __getattr__(self, attrname):
            print('Trace: ' + attrname)  # Catches all but own attrs
            self.fetches += 1
            return getattr(self.wrapped, attrname)  # Delegate to wrapped obj

    return Wrapper


if __name__ == '__main__':
    @Tracer
    class Spam:  # Spam = Tracer(Spam)
        def display(self):  # Spam is rebound to Wrapper
            print('Spam!' * 8)


    A = Spam()
    A.display()
    print(A.fetches)
