# packing and unpacking arguments in Python
# https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/


(a, b, c) = (1, 2, 3)

print(a)

x, y, z = (4, 5, 6)

print(y)

r, t, g = 8, 9, 10

print(g)

a1, b1, c1 = "abc"

print(b1)

a2, b2, c2 = [1, 2, 3]

print(c2)

g = (i for i in range(3))
print(g)
w1, w2, w3 = g

q1, q2, q3 = (i for i in range(3))

print(q3)

d = {'key a': 100, 'key b': 200, 'key c': 300}
e1, e2, e3 = d  # to get key
print(e1)

e4, e5, e6 = d.values()  # to get values
print(e4)

e7, e8, e9 = d.items()  # to get keys and values
print(e9)

key, value = e8
print(key)


# unpacking functions
d = {'key a': 100, 'key b': 200, 'key c': 300}
a1, a2, a3 = d.items()  # to get key


def f(a, b):
    print(a, b)


f(*a1)


#
d = {'a': 100, 'b': 200, 'c': 300}


def f(a, b, c):
    print(a, b, c)


f(*d)  # for keys
f(*d.values())  # for values
f(*d.items())  # for keys and values
f(**d)


# PACKING DATA

*a, = 1, 2
print(*a)

c, *d = 100, 200, 300
print(*d)

*e, f, g, h = 6, 7, 8
print(type(e))

#
gen = (i for i in range(5))
*g, = gen

print(g)

#

items = ['mykola', 'bob', 'candy']

a1, a2, a3 = items
print(a1, a2, a3)

#
g = 8
l = 9
g, l = l, g
print(g, l)

#
a, b, *trash = 1, 2, 0, 0, 0
print(trash)

#
data1 = {'a': 100, 'b': 200, 'c': 300}
data2 = {'d': 400, 'e': 500, 'f': 600, 'a': 200}  # 100 will be replaced by 200

res = {**data1, **data2}
print(res)

#

def f1():  # endpoint1
    return [('phone', 100), ('laptop', 2000), ('ID:324', 'toy', 555)]

def f2():  # endpoint2
    data = f1()
    for *trash, item, price in data:
        print(item, price)


f2()