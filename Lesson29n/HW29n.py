# HW on queue

import sys


# *** NODE SECTION ***
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# *** MENU SECTION ***
def menu():
    choice = 0
    while choice != 6:
        print(f"\n \t Menu:"
              f"\n[1] IsEmpty"
              f"\n[2] IsFull"
              f"\n[3] Enqueue"
              f"\n[4] Dequeue"
              f"\n[5] Show"
              f"\n[0] Exit")
        choice = int(input(f'\nPlease enter option from the menu: '))
        match choice:
            case 1:
                IsEmpty()
            case 2:
                IsFull()
            case 3:
                Enqueue()
            case 4:
                Dequeue()
            case 5:
                Show()
            case 0:
                exit_program()


def IsEmpty():
    pass
    print('\nExecuted.')
    go_on()


def IsFull():
    pass
    print('\nExecuted.')
    go_on()


def Enqueue():
    pass
    print('\nExecuted.')
    go_on()


def Dequeue():
    pass
    print('\nExecuted.')
    go_on()


def Show():
    pass
    print('\nExecuted.')
    go_on()


def exit_program():
    print('\nSession terminated')
    sys.exit()


def go_on():
    print('\nDo you want to continue? [Y/N]')
    selection = str(input('>>>')).lower()
    if selection == 'n':
        exit_program()
    else:
        pass


# invoke menu
menu()
