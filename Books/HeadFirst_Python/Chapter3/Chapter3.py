# STRUCTURED DATA
import pprint

person3 = {
    'Name': 'Ford',
    'Gender': 'Male',
    'Occupation': 'Researcher',
    'Home Planet': 'Betelgeuse Seven'
}

# accessing data
print(person3)
print(person3['Name'])

# adding a row

person3['Age'] = 33

print(person3)

# adding key pairs
found = {}
found['o'] = 0
found['i'] = 0
found['e'] = 0
found['a'] = 0
found['u'] = 0

print(found)

# changing key pairs
found['e'] = found['e'] + 1
print(found)

# or

found['e'] += 1
print(found)

# ITERATING OVER A DICTIONARY to process keys
print('\nExercise: Iterating over a dictionary to process KEYS')
for kv in found:
    print(kv)

# iterating over a dictionary to process values only
print('\nExercise: Iterating over a dictionary to process VALUES')
for i in found:
    print(found[i])

# iterating over a dictionary to process keys and values
print('\nExercise: Iterating over a dictionary to process KEYS and VALUES')
for k in found:
    print(k, 'was found', found[k], 'times.')

# sorting dictionaries
print('\nExercise: sorting')
for k in sorted(found):
    print(k, 'was found', found[k], 'times.')

# sorting dictionaries
print('\nExercise: sorting with method .items()')
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'times.')

# test drive
print('\nExercise: test drive')
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
for letter in word:
    if letter in vowels:
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

# SETS
print('\nExercise: SETS')
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)
print(type(vowels))

# exercise 1
print('\nExercise: creating new set by merging sets')
# vowels = { 'a', 'e', 'e', 'i', 'o', 'u', 'u' }
vowels = set('aeiou')
word = 'hello'
u = vowels.union(set(word))
print(u)

# exercise 2
print('\nExercise: creating new set by comparing sets and excluding the same values')
d = vowels.difference(set(word))
print(d)

# exercise 3
print('\nExercise: creating new set by comparing sets and show common values')
i = vowels.intersection(set(word))
print(i)

# TUPLES (immutable)
print('\nExercise: TUPLES')
vowels2 = ('a', 'e', 'i', 'o', 'u')
print(vowels2)
print(type(vowels2))

# comparison
print('\nExercise: comparison of classes')
list_of_values = ['a', 'b']
dictionary_of_values = {'a': 'first,',
                        'b': 'second'}
set_of_values = {'a', 'b', 'b', 'c'}
tuple_of_values = ('a', 'b')
print(type(list_of_values))
print(type(dictionary_of_values))
print(type(set_of_values))
print(type(tuple_of_values))

# Dictionary of dictionaries
print('\nExercise: dictionary in dictionary')
dict_in_dict = {'first': {'name': 'John',
                          'surname': 'Smith'},
                'second': {'name': 'Jane',
                           'surname': 'Dow'}}
print(dict_in_dict)
print(type(dict_in_dict))

# user friendly printing of dictionary in dictionary
import pprint
pprint.pprint(dict_in_dict)
