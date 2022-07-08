# list [] editable, not unique

# tuple () not editable

t = (4, 5, 6)

for i in t:
    print(i)


def askPersonalInfo():
    while True:
        firstName = input("Input your first name:")
        lastName = input("Input your last name:")
        yearBirth = input("Input your year of birth:")
        gender = input("Input your gender (M,F):")
        if firstName == "" or lastName == "" \
                or yearBirth == "" \
                or gender == "" \
                or gender not in ('F', 'M'):
            print("Wrong data!")
        else:
            return firstName, lastName, yearBirth, gender


# personalInfo = askPersonalInfo()
# print(personalInfo)

# set {} unique

# Option 1:
user = {"Mykola", 39}

# Option 2 (constructor)
ls = ['Valeriia', 29]
user2 = set(ls)

print(user)
print(user2)

print(f'number of elements is: {len(user)}')

# removing value
ls2 = {'Alex', 'Bob', 'Sam'}
print(ls2)

ls2.remove('Sam')
print(ls2)

# removing all values

ls2.clear()
print(ls2)

# iterating sets

s = {4, 5, 3, 2, 1}
for i in s:
    print(i, end=" ")

#
print('\n Merging sets:')
s1 = {4, 5, 6, 7, 8, 9, 0}
s2 = {1, 2, 3, 4, 5}

res = s1.union(s2)
print(res)

print('\n Finding difference in sets:')
res1 = s1.difference(s2)
print(f'Values missing in s1: {res1}')

print('\n Finding intersection of sets:')
res2 = s1.intersection(s2)
print(f'Values present in both sets: {res2}')

print('\n Finding unique values in sets:')
res3 = s1.symmetric_difference(s2)
print(f'Values unique in both sets: {res3}')

#
f = frozenset([1, 3, 3, 4, 5])
for i in f:
    print(i, end=" ")

# dictionary {key:value}
print('\n\nCreate dictionary - Option 1:')
d = {1: 'val1', 2: 'val2', 3: 'val3', 4: 'val4'}
print(d)

print('\nCreate dictionary - Option 2:')
ls5 = [
    [1, 'a'],
    [2, 'b']
]
d2 = dict(ls5)
print(d2)

# extracting  values
print('\n Extracting value without key:')
print(d[1])

# extracting all keys
print('\n Extracting all keys:')
print(*d)

# iterating through dictionary
print('\n Iterating through dic:')

for key, val in d.items():
    print(f'{key} - {val}')

# removing elements
print('\n Removing elements from dictionary:')
item_to_remove = 1
if item_to_remove in d:
    del d[item_to_remove]
print(d)
