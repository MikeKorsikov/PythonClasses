'''
Deserialization is the process of decoding the data that is in JSON
format into native data type.
'''
# https://www.geeksforgeeks.org/deserialize-json-to-object-in-python/

# importing the module
import json

# creating the JSON data as a string
data = '{"Name" : "Romy", "Gender" : "Female"}'

print("Datatype before deserialization : "
      + str(type(data)))

# deserializing the data
data = json.loads(data)

print("Datatype after deserialization : "
      + str(type(data)))

# (2) opening the JSON file
data = open('datafile.json', )

print("Datatype before deserialization : "
      + str(type(data)))

# deserializing the data
data = json.load(data)

print("Datatype after deserialization : "
      + str(type(data)))
