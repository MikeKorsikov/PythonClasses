#

def showAllView(my_list):
    print(f'In db we have {len(my_list)} people. Which are:')
    for person in my_list:
        print(person)


def index():
    print('Home page')
    print('Do you want to see all? [y/n]')


def endView():
    print('Goodbye.')


def errorView():
    print('Error message')
