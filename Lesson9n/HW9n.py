# sorting part of the list

print('Exercise 1 - Sorting fraction of the list')

# given list can be adjusted
given_list = [1, -2, 13, 4, -5, 0, 6, -7, 8, -9, 230, -4500]
TT_list = []
OT_list = []
adjusted_list = []

sum_of_digits = 0
count = 0
num_of_items = len(given_list)

print(f'\nList prior sorting: {given_list}')
print(f'Number of items in a list is: {num_of_items}.')

for i in given_list:
    sum_of_digits += i
    count += 1

average_result = round(sum_of_digits / count, 2)
print(f'Average is: {average_result}.')

if average_result > 0:
    print('\nAs long as average is greater than 0, we do the following: ')

    two_thirds = round(num_of_items / 3 * 2)
    print(f'(1) Index of 2/3 of the list is: {two_thirds}')

    for x in range(0, two_thirds):
        TT_list.append(given_list[x])
        TT_list.sort(reverse=False)
    print(f'\n(2) Two thirds of the list sorted: {TT_list}')

    print('\n(3) Extracting remaining 1/3 of the given list:')
    for x in range(two_thirds, num_of_items):
        OT_list.append(given_list[x])
    print(f'\tExtracted 1/3 is: {OT_list}')

    OT_reversed = []
    for x in OT_list:
        OT_reversed.insert(0,x)
    print(f'\n(4) Remaining 1/3 of the given list in reversed order: {OT_reversed}')

    print('\n(5) Joining two lists together:')
    adjusted_list = TT_list + OT_reversed
    print(f'\t{adjusted_list}')

else:
    print('\nAs long as average is less than 0, we do the following: ')

    one_third = round(num_of_items / 3)
    print(f'(1) Index of 2/3 of the list is: {one_third}')

    for x in range(0, one_third):
        TT_list.append(given_list[x])
        TT_list.sort(reverse=False)
    print(f'\n(2) One third of the list sorted: {TT_list}')

    print('\n(3) Extracting remaining 2/3 of the given list:')
    for x in range(one_third, num_of_items):
        OT_list.append(given_list[x])
    print(f'\tExtracted 2/3 is: {OT_list}')

    OT_reversed = []
    for x in OT_list:
        OT_reversed.insert(0,x)
    print(f'\n(4) Remaining 2/3 of the given list in reversed order: {OT_reversed}')

    print('\n(5) Joining two lists together:')
    adjusted_list = TT_list + OT_reversed
    print(f'\t{adjusted_list}')