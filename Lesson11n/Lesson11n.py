# sorting data (part 3)
#
# ls = [5, 6, 8, 4, 1, 9, 0]
# answer = 1
#
# for i in ls:
#     if i == answer:
#         print('Found')
#
#
# l1 = [3, 5, 1]
# l2 = [6, 9, 0, -6]
# l3 = [0, 0, 1]
# l4 = [4, 7, 2, 1]
#
# temp = l1 + l2 + l3 + l4
# print(temp)
#
# final = []
#
# for i in range(len(temp)):
#     if temp[i] not in final:
#         final.append(temp[i])
#
# print(final)


def sorting_books():
    list_of_books = ['Actually first', 'Better known as second', 'Can be called third']
    list_of_years = [2022, 1983, 1917]
    option = input('Select how you want to sort list (Y - years, B - books):')

    if option.upper() == 'Y':
        list_of_years, list_of_books = zip(*sorted(zip(list_of_years, list_of_books)))
        for i in range(len(list_of_books)):
            print(f'{list_of_years[i]} - {list_of_books[i]}')
    else:
        list_of_books,list_of_years = zip(*sorted(zip(list_of_books, list_of_years)))
        for i in range(len(list_of_books)):
            print(f'{list_of_books[i]} - {list_of_years[i]}')


sorting_books()