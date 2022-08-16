# anotations

def search4vowels(phrase: str) -> set:
    """Return any vowels found in supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


# print(search4vowels("mykola"))

def search4letters(phrase: str, letters: str) -> set:
    return set(letters).intersection(set(phrase))


# print(search4letters('I love the world the way it is', 'oa'))

# print(set('mykola'))

# assigning default values to arguments

def search4letters2(phrase: str, letters: str = 'aoiue') -> set:
    return set(letters).intersection(set(phrase))

print(search4letters2('mykola'))