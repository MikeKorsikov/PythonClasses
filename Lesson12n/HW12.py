# Exercise 1
print('\t\t\t*** Exercise 1 intersection for three tuples ***\n')

ls1 = (0, 1, 3, 4, 6, 7, 9)
ls2 = (0, 2, 3, 6, 7, 9, 10)
ls3 = (0, 2, 3, 4, 6, 8, 9)

ls4 = tuple(set(ls1) & set(ls2) & set(ls3))
print(f'List 1: {ls1}')
print(f'List 2: {ls2}')
print(f'List 3: {ls3}')
print(f'Intersection of three tuples is: {ls4}')

# TEST:
print('\nChecking results:')
test1 = tuple(set(ls1).intersection(set(ls2)))
test2 = tuple(set(ls2).intersection(set(ls3)))
print('Intersection of ls1 and ls2: ', test1)
print('Intersection of ls2 and ls3: ', test2)

test3 = tuple(set(test1).intersection(set(test2)))
print('Intersection of two intersections:', test3)

test4 = test3 == ls4
print(f'Results of indentifying intrsection are accurate: {test4}\n')

# Exercise 2
print('\t\t\t*** Exercise 2 identifying unique elements in three tuples ***\n')

sl1 = (0, 1, 2, 333)
sl2 = (0, 1, 2, 444)
sl3 = (0, 1, 2, 555)

print(f'List 1: {sl1}')
print(f'List 2: {sl2}')
print(f'List 3: {sl3}')

ul = []
for i in sl1:
    if i not in sl2 and i not in sl3:
        ul.append(i)
for i in sl2:
    if i not in sl3 and i not in sl1:
        ul.append(i)
for i in sl3:
    if i not in sl1 and i not in sl2:
        ul.append(i)
print(f'Following values are unique to each list: {tuple(ul)}')

# TEST (using iteration)
print('\nChecking results:')

# finding non-unique
sl4 = tuple(set(sl1) & set(sl2))
sl5 = tuple(set(sl2) & set(sl3))
sl6 = tuple(set(sl4 + sl5))

# generate combines list
sl7 = set(sl1 + sl2 + sl3)

# compare non-unique and combined list
sl8 = tuple(set(sl6) ^ set(sl7))

print(f'Unique values in three lists are: {sl8}')
test5 = set(ul) == set(sl8)
print(f'Results of identifying unique values are accurate: {test5}\n')

# Exercise 3
print('\t\t\t*** Exercise 3 identifying the same values in the same index place ***\n')
ll1 = (4, 3, 2, 1, 5)
ll2 = (1, 3, 2, 4, 5)
ll3 = (1, 4, 2, 3, 5)
ll4 = []
li4 = []

print('List 1:', ll1)
print('List 2:', ll2)
print('List 3:', ll3)

for i in ll1:
    for j in range(0, len(ll1)):
        # j is index in the list -> 0, 1, 2, 3, 4
        # print(f'J{j} - {ll3[j]}')
        if i == ll1[j] and i == ll2[j] and i == ll3[j]:
            ll4.append(i)
            li4.append(j)

print('\nThe same values across all three tuples which share the same index:')
for i in range(0,len(ll4)):
    print(f'Value: {ll4[i]} and Index: {li4[i]} ')
