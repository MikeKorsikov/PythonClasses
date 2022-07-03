# functions (continued) - recursion

import random as r

ls = [1, 2, 3, 4, 5]
a = r.random()
b = r.randint(5, 50)
c = r.choice(ls)
d = r.shuffle(ls)
e = r.randrange(1, 50, 1)

print(a)
print(b)
print(c)

print('Shaffle:')
print(ls)

print(e)

# types
print('\nTypes:')
print(type(5))

def foo():
    pass
print(type(foo))

print('\n Functions within functions:')
def gen(answ):
    if answ.find('check'):
        return foo1(5, 9)
    elif answ.find('p'):
        return foo2(5, 5)

def foo1(a, b):
    return a != 0 and a > b > 0

def foo2(a, b):
    return a**b

print(gen('check'))

# recursion
print('\nRecursion:')
def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)

print(fact(5))

# anonymous functions
print('\nLambda function:')
myNumbers = [1, 2, 3, 4, 5]
newNum = lambda x:x+10

for num in myNumbers:
    print(newNum(num))


studBirthYear = [2000, 1997, 2002, 1999, 2007]
studAges=list(map(lambda x:2022-x,studBirthYear))
print(studAges) # [22, 25, 20, 23, 15]

numbersList1 = [10, 20, 30]
numbersList2 = [1, 2, 3]
result = map(lambda a, b: a**b, numbersList1, numbersList2)
print(list(result)) #[10, 400, 27000]

prices=[100.45, 8.56, 5, 234, 45, 87, 567]
expensive=list(filter(lambda x:x>=10, prices))
print(expensive) #[100.45, 234, 45, 87, 567]

list1=[1,2,3,4,5]
print(list(zip(list1)))
#[(1,), (2,), (3,), (4,), (5,)]
print(list(zip())) #[]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
print(list(zip(list1,list2)))
#[(1, 'a'), (2, 'b'), (3, 'c')]


from functools import partial
def showWord(myStr, n):
    return myStr*n

tripleMyltipleText = partial(showWord, 3)
print(tripleMyltipleText("Mykola"))

