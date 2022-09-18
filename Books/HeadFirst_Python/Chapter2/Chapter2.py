# LIST DATA (list, tuple, dictionary, set)

import random

wait_time = random.randint(1, 60)

# LIST - an ordered mutable collection of objects

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

prices = []
odds_and_ends = [[1, 2, 3],
                 ['a', 'b', 'c'],
                 ['one', 'two', 'three']]

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

# identifying length of list
print(len(found))

# adding object to list
found.append('a')
print(len(found))
print(found)

# removing objects from list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums.remove(3)
print(nums)

# removing objects from list with POP()
nums.pop(0)
print(nums)

# extending list with another list
nums.extend([11, 12])
print(nums)

# inserting object in the list: insert(1st - index, 2nd - value)
nums.insert(0, 1)
print(nums)

nums.insert(2, 'three')
print(nums)

# insert does not replace but extends list if there is already value
nums.insert(0, 0)
print(nums)

# to know more run: help(list)
# help(list)

# converting string to list

phrase = "Don't panic!"
plist = list(phrase)
print(plist)

# copying lists with .copy()

first = [1, 2, 3, 4, 5]
second = first
second.append(6)
third = first.copy()
third.append(7)

print(first)
print(second)
print(third)

# referencing to index values first [0] and last [-1]

saying = "Don't panic!"
letters = list(saying)
print(letters)
print(letters[0])
print(letters[-1])

# manipulating lists
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

# looping through the lists

paranoid_android = "Marvin"
letters = list(paranoid_android)
for character in letters:
    print('\t', character)
print()
# looping through the lists and slicing them

paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for character in letters[0:6]:
    print('\t', character)
print()
for character in letters[-7:]:
    print('\t'*2, character)

for character in letters[12:20]:
    print('\t'*3, character)
print()

# TUPLE - an ordered immutable collection of objects (constant list)

# DICTIONARY - an unordered set of key/value pairs

# SET - an unordered set of unique objects

