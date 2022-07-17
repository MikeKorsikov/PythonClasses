import json

#
str_j = '{"name":"Alex", "age":"12"}'

j = json.loads(str_j)

print(j['name'])
