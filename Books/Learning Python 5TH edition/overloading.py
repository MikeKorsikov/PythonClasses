# indexing


class Indexer:
    def __getitem__(self, index):
        return index ** 2


# example 1
X = Indexer()
print(X[2])

# example 2
for i in range(5):
    print(X[i], end='')



# obtaining value using key/index
class Indexer2:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print(f"Key [{index}] has value [{self.data[index]}].")


# example
Y = Indexer2()
Y[0]
Y[-1]
Y[2:4]


# Index iteration
class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]  # data is supplied after object is initialized


# example
Z = StepperIndex()
Z.data = "ABCDEFG"
print(Z[1])

for item in Z:
    print(item, end=' ')




class Squares:
    def __init__(self, start, stop):  # Non-yield generator
        self.start = start  # Multiscans: extra object
        self.stop = stop

    def __iter__(self):
        return SquaresIter(self.start, self.stop)


class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


# example
S = Squares(1, 5)
I = iter(S)
print(next(I), next(I))

for i in S:
    print(i)



# __getattr__
class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)


#example
X = Empty()
print(X.age)
print(X.name)



# __setattr__
class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr + ' not allowed')

# example
X = Accesscontrol()
X.age = 40
print(X.age)
X.name = 'Bob'
print(X.name)


# __call__
class Calle:
    def __call__(self, *pargs, **kargs):
        print('Called:', pargs, kargs)


# example
C = Calle()
C(1, 2, 3)

D = Calle()
D(1, 2, 3, x=4, y=5)


# __call_ is usefull with APIs
class Prod:
    def __init__(self, value):  # Accept just one argument
        self.value = value

    def __call__(self, other):
        return self.value * other

x = Prod(2)
print(x(3))