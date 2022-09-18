# FUNCTIONS AND MODULES
# page 185 of 624

# functions without argument
def search4vowels1():
    """display any vowels found in asked-for word"""
    vowels = set('aeiou')
    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


# search4vowels1()

# functions with argument
def search4vowels2(word):
    """display any vowels found in asked-for word"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


# search4vowels2('mykola')

# True and False
print('\nExamples of False:')
print('0 is:', bool(0))
print('0.0 is:', bool(0.0))
print('"" is:', bool(""))
print('[] is:', bool([]))
print('{} is:', bool({}))
print('None is:', bool(None))

print('\nExamples of True:')
print('1 is:', bool(1))
print('-1 is:', bool(-1))
print('42 is:', bool(42))
print('0.01 is:', bool(0.01))
print('"Panic" is:', bool("Panic"))
print('[42, 43, 44] is:', bool([42, 43, 44]))
print("{'a': 42, 'b': 42} is:", bool({'a': 42, 'b': 42}))


# functions with argument using return
def search4vowels(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


search4vowels('mykola')

