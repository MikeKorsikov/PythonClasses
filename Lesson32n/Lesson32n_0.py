# packing and unpacking arguments in Python (part 2)
# https://www.w3schools.com/python/python_json.asp
# https://www.geeksforgeeks.org/read-json-file-using-python/

import json

FILE = "data.json"

data = {
    "Name": "Mykola",
    "Exams": {
        "Math": 100,
        "CS": 100
    },
    "age": 20,
    "alive": True
}

try:
    f1 = open(FILE, "w")
    f1.write(json.dumps(data, indent=4))
    f1.close()

except Exception as e:
    print(str(e))

#
ls = []
try:
    f1 = open(FILE, "r")
    ls = json.loads(f1.read())
    f1.close()

except Exception as e:
    print(str(e))

#
print(ls)
print(ls.get('Name'))
