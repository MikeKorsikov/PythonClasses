# Iterator design pattern

class IIterator:
    @staticmethod
    def has_next():
        pass

    @staticmethod
    def next():
        pass


class Iterator(IIterator):
    def __init__(self, collection):
        self.index = 0
        self.collection = collection

    def next(self):
        if self.has_next():
            obj = self.collection[self.index]
            self.index += 1
            return obj
        raise Exception('End of iterator')

    def has_next(self):
        return self.index < len(self.collection)


#
class IPerson:
    @staticmethod
    def method():
        pass


class Person1(IPerson):
    @staticmethod
    def method():
        print('Call from Person1')


class Person2(IPerson):
    @staticmethod
    def method():
        print('Call from Person2')


Persons1 = [Person1(), Person1(), Person1(), Person1()]
Persons2 = [Person2(), Person2(), Person2(), Person2()]

Iter = Iterator(Persons1)


# alternatively
for i in Persons1:
    i.method()

# alternatively
while Iter.has_next():
    Iter.next().method()