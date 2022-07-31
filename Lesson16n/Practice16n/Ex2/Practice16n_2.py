import pickle
import csv

print('Exercise 2: ')

file_name = 'text.txt'
name = 'Alex'
age = 30
person = {'name': 'Alex', 'age': '30', 'city': 'Lviv'}

print('\n1) Dumping and loading data:')
with open(file_name, 'wb') as f:
    pickle.dump(name, f)
    pickle.dump(age, f)

with open(file_name, 'rb') as f:
    n1 = pickle.load(f)
    a1 = pickle.load(f)

print(n1, a1)

#
print('\n2) Dumping and loading using dictionary:')
with open(file_name, 'wb') as f:
    pickle.dump(person, f)

with open(file_name, 'rb') as f:
    data = pickle.load(f)

print(data['name'], data['age'])

#
print('\n3) Dumping and loading in csv using dictionary:')
file_name = 'data.csv'
person = [
    {'name': 'Alex', 'age': '30', 'city': 'Lviv'},
    {'name': 'Mykola', 'age': '30', 'city': 'Lviv'},
    {'name': 'Oleh', 'age': '30', 'city': 'Lviv'}
]

with open(file_name, 'w') as f:
    columns = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(person)

#
with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i['name'] + '\t' + i['age'] + '\t' + i['city'])

#
print('\n4) Dumping and loading in csv using list:')
file_name = 'data2.csv'
person = ['Alex', '28', 'Lviv']
with open('data2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(person)

with open('data2.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)