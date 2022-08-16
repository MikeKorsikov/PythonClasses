# class ExampleClass:
#     def __init__(self, val=1):
#         self.__first = val
#
#     def set_second(self, val):
#         self.__second = val
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
#
# example_object_2.set_second(3)
#
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5
#
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)
#
# print(example_object_1._ExampleClass__first)
#
# # Class variables
# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
#
#
# example_object_1 = ExampleClass()
# print(example_object_1.__dict__, example_object_1.counter)
#
# example_object_2 = ExampleClass(2)
# print(example_object_2.__dict__, example_object_2.counter)
#
# example_object_3 = ExampleClass(4)
# print(example_object_3.__dict__, example_object_3.counter)
#
# class ExampleClass:
#     varia = 1
#     def __init__(self, val):
#         ExampleClass.varia = val
#
#
# print(ExampleClass.__dict__)
# example_object = ExampleClass(2)
#
# print(ExampleClass.__dict__)
# print(example_object.__dict__)
#
# #
# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object = ExampleClass(1)
# print(example_object.a)
#
# if hasattr(example_object, 'b'):
#     print(example_object.b)
#
# #
# class ExampleClass:
#     attr = 1
#
# print(hasattr(ExampleClass, 'attr'))
# print(hasattr(ExampleClass, 'prop'))
#
#
# # 3.4.1.1
# class Classy:
#     def method(self, par):
#         print('method:', par)
#
# obj = Classy()
#
# obj.method(1)
#
# #
# class Classy:
#     def __init__(self, value = None):
#         self.var = value
#
#
# obj_1 = Classy("object")
# obj_2 = Classy()
#
# print(obj_1.var)
# print(obj_2.var)

# # Hiding methods
# class Classy:
#     def visible(self):
#         print("visible")
#
#     def __hidden(self):
#         print("hidden")
#
#
# obj = Classy()
# obj.visible()
#
# try:
#     obj.__hidden()
# except:
#     print("failed")
#
# obj._Classy__hidden()

#
