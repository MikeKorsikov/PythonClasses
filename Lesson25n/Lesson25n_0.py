# class Number:
#     MIN_NUMBER = 0
#     MAX_NUMBER = 10
#
#     def __init__(self, num):
#         self.num = None
#         if type(num) == int and self.check(num):
#             self.num = num
#         else:
#             print('Error type')
#
#     @classmethod
#     def check(cls, num):
#         return cls.MIN_NUMBER < num < cls.MAX_NUMBER
#
#     @staticmethod
#     def mult(n1, n2):
#         return n1 * n2
#
#
# n1 = Number(2)
# Number.MIN_NUMBER = 5
# print(n1.check(2))


# (descriptors)
class Number:  # descriptor
    def __set_name__(self, owner, name):  # owner is a class
        self.var = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.var]

    def __set__(self, instance, value):
        instance.__dict__[self.var] = value


class Point3D:  # using descriptor
    x = Number()  # self._x
    y = Number()
    z = Number()

    def __init__(self, x, y, z):
         self.x = x
         self.y = y
         self.z = z

    # @property
    # def x(self):
    #     return self.x
    #
    # @x.setter
    # def x(self, value):
    #     self.x = value
    #
    # @property
    # def y(self):
    #     return self.y
    #
    # @y.setter
    # def y(self, value):
    #     self.y = value
    #
    # @property
    # def z(self):
    #     return self.z
    #
    # @z.setter
    # def z(self, value):
    #     self.z = value


p1 = Point3D(1, 2, 3)
# testing getter
print(p1.x)

# testing setter
p1.x = 5
print(p1.x)