#Option 1
import random

#Option 2
#from random import *


print('Hello World')

print('one', 'two', 'three', sep=', ', end=' ')
print('four')
print(2 + 2)


# comment (type 1)

'''
comments (type 2)
'''


number = 10

name = input('Enter your name: ')

num1 = int(input('Enter first num: '))
num2 = int(input('Enter first num: '))
# num3 = input('Enter first num: ')
result = num1 + num2
print('Sum is: ', num1 + num2)
print('Type: ', type(result))

words = 'Hello \n \t world'
print(words)

words = 'Hello \\n\\ \\t\\ \'world'
print(words)

# example3:

name = 'Mykola'
age = 39

# Option1
print('Name: {}\nAge: {}'.format(name, age))
# Option2
print(f'Name: {name}\n Age: {age}')


#importing specific library
#see above

num = random.random()
print(num)

num1 = random.randint(1, 10)
print(num1)



num1 = 10
num2 = 8

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2) #to power of
print(num1 // num2) #whole after devision
print(num1 % num2) #reminder after devision


# number = 10
# number += 2
# number **= 2
# print(number)
