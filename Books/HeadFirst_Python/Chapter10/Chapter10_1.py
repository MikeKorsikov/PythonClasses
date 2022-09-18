# nesting function inside function

def apply(func: object, value: object) -> object:
    return func(value)


apply(print, 42)
print(apply(id, 42))
print(apply(type, 42))
print(apply(len, 'Marvin'))
print(apply(type, apply))

# Option 1
print('\nOption 1 - returning function from function')


def outer():
    def inner():
        print('This is inner.')

    print('This is outer, invoking inner.')
    inner()


outer()

# Option 2
print('\nOption 2 - returning function from function [with return]')


def outer2():
    def inner():
        print('This is inner.')

    print('This is outer, return inner.')
    return inner


i = outer2()
print(type(i))
i()


# passing arguments to function
print('\nIntroducing flexible number of arguments in a function with *')
def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

print('\nNo arguments:')
myfunc()
print('\nOne argument:')
myfunc(10)
print('\nMultiple arguments:')
myfunc(10, 20, 30)

print('\nExpanding the list:')
values = [1, 2, 3, 4, 5]
print('a) with NO *, it is a single object:')
myfunc(values)

print('\nb) with *, list expands to individual arguments:')
myfunc(*values)

print('\nUse of "kwardgs" with **:')


# ** tells the function to expect keyword arguments (dictionary with key pairs)

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


myfunc2(a=10, b=20)

# combining *args and **kwargs
print('\nUse of *args and **kwargs in one function:')

def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()


print('\nNo arguments:')
myfunc3()
print('\nSeveral arguments:')
myfunc3(1, 2, 3)
print('\nKeyword arguments:')
myfunc3(a=10, b=20, c=30)
print('\nCombination of list and keyword arguments:')
myfunc3(1, 2, 3, a=10, b=20, c=30)