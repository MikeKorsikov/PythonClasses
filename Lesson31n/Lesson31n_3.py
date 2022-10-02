'''
 The pickle module implements binary protocols for serializing and
 de-serializing a Python object structure.

 Used for python projects only.
'''
# https://www.geeksforgeeks.org/understanding-python-pickling-example/

import pickle

data = {'A': {'d': 400, 'e': 500, 'f': 600, 'a': 200},
        'B': {'d': 400, 'e': 500, 'f': 600, 'a': 200}}

with open('text.txt', 'wb') as file:
    pickle.dump(data, file)

with open('text.txt', 'rb') as file:
    new = pickle.load(file)

print(new)
