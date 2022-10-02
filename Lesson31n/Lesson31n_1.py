'''
 Serialization refers to the process of converting a data object (e.g., Python objects,
 Tensorflow models)  into a format that allows us to store or transmit the data and
 then recreate the object when needed using the reverse process of deserialization.
'''
# https://www.geeksforgeeks.org/serializing-json-data-in-python/

# import module
import json

# Data to be written
data = {
    "user": {
        "name": "satyam kumar",
        "age": 21,
        "Place": "Patna",
        "Blood group": "O+"
    }
}

# Serializing json and
# Writing json file
with open("datafile.json", "w") as write:
    json.dump(data, write)

# Data to be written
data = {
    "user": {
        "name": "satyam kumar",
        "age": 21,
        "Place": "Patna",
        "Blood group": "O+"
    }
}

# Serializing json
res = json.dumps(data)
print(res)
