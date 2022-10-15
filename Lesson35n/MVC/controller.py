#
from model import People
from view import showAllView, index, endView, errorView


def showall():
    people_in_db = People.getAll()
    return showAllView(people_in_db)


def main():
    index()
    answer = input()
    if answer == 'y':
        return showall()
    elif answer == 'n':
        return endView()
    else:
        return errorView()


if __name__ == '__main__':
    main()
