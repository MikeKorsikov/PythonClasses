# @property -> getter

class Number:
    def __init__(self, n):
        self.__n = n

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        self.__n = value

    @n.deleter
    def n(self):
        del self.__n



n1 = Number(5)
print(n1.n)

n1.n = 10
print(n1.n)

