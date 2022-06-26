# list/array []

ls = ['Hello', 45, True]
ls2 = list()

print(ls[2])

# changing list
ls[1] = 1.005
print(ls[1])

# printing elements of list
i = 0
while i < 3:
    print(ls[i])
    i += 1

ls3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]
copy_ls = ls3 [3:7:1]
print(copy_ls)

copy_ls = ls3 [7:3:1]
print(copy_ls)

print(len(ls3))

# methods:
# ls3.append(4)
# ls3.insert(1, 2)
# ls3.pop(10)
# ls3.clear()

if 5 in ls3:
    ls3.remove(5)
print(ls3)

ls_count = ls3.count(9)
print(ls_count)

# referencing lists
ls4 = ls3

# to copy list
print('\nCopy lists:')
ls5 = ls3.copy()
ls3.clear()
print(ls5, ls3)

# list in lists
print('\nList in list:')
people = [
    ['Tom', 29],
    ['Alice', 34],
    ['Mykola', 67]
]

print(people[0])

