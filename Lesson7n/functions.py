# functions
import math
import test

# importing functions from other modules
a = 4
b = 2

c = math.sqrt(a)
d = math.pow(b, a)
print(c)
print(d)

# importing data from other modules
a = test.LOGIN
b = test.PASSWORD
print(a, b)


# installing modules via pip (check if you have: pip --version)
# todo
# 1 - scratch balls
# 2 - have a beer
# 3 - write awesome code

# Exercise:
# 12345 -> 123,456

def funct(num, sep=''):
    """code"""

# multiple parameters
def foo(*num):
    print(num)

foo(10, 20, 30)

def foo2(*num):
    global ls
    ls = list()
    for i in num:
        ls.append(i)

    print(ls)

foo2(1, 2, 3, 4, 5, 6)
print(ls)

# **kwargs (read more!)
def foo3(*num, **kwargs):
         """code"""
         print(kwargs)
         for key, val in kwargs.items():
             print(f'{key} -> {val}')


foo3(10, 20, 30, name='alex', age='20')

# return - stops function but enable to save result of function
def foo5(a, b):
    global x_var
    x_var = a + b
    return x_var

res = foo5(2, 3)
print(res)


