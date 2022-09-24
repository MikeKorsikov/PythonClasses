# wrapper


class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)


# example
x = Wrapper([1, 2, 3])
x.append(4)
print(x.wrapped)


# Option 1
class Sum:
    def __init__(self, val):  # Callable instances
        self.val = val

    def __call__(self, arg):
        return self.val + arg


# Option 2
class Product:
    def __init__(self, val):  # Bound methods
        self.val = val

    def method(self, arg):
        return self.val + arg


# example
Sobject = Sum(2)
print(Sobject(40))

Pobject = Product(2)
print(Pobject.method(40))


# __repr__
class Spam:
    def __init__(self): # No __repr__ or __str__
        self.data1 = "food"


class Spam2:
    def __init__(self): # No __repr__ or __str__
        self.data1 = "food"

    def __repr__(self):
        return self.data1


# example
X = Spam()
print(X)

Y = Spam2()
print(Y)


# use of __str__ from one class in another class for convenient print()
class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,  # My class's name
            id(self),  # My address
            self.__attrnames())  # name=value list


if __name__ == '__main__':
    class Spam(ListInstance):
        def __init__(self):
            self.data1 = 'food'


    X = Spam()
    print(X)


#
class MyList(list):
    def __getitem__(self, index):
        print('(indexing %s at %s)' % (self, index))
        return list.__getitem__(self, index - 1)


if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc') # __init__ inherited from list
    print(x) # __repr__ inherited from list
    print(x[1]) # MyList.__getitem__
    print(x[3]) # Customizes list superclass method
    x.append('spam'); print(x) # Attributes from list superclass
    x.reverse(); print(x)

