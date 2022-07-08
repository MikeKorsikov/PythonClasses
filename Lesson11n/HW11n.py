# sorting lists by book title and by year published

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