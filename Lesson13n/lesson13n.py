# dictionary
import json

d = {'a': 1, 'b': 2, 'c': 3}

d1 = d.copy()

print(d)
print(d1)

print('Removing original dictionary')
d.clear()
print(d)
print(d1)

# Dictionary in dictionary
print('\nDictionary in dictionary:')
person = {
    "Alex": {
        "email": "alex@gmail.com",
        "age": 35
    },
    "John": {
        "email": "john@yahoo.com",
        "age": 47
    }
}

# getting values of dictionary
print(person["Alex"])
print(person["John"]["age"])


# iterating through item of dictionary
for key, val in person["Alex"].items():
    print(f"{key} - {val}")

# iterating through all items of dictionary
for key, val in person.items():
    print(f"{key} - {val}")

# converting dictionary to JSON
j1 = json.dumps(person)
print(j1)