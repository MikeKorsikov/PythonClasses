# HW on queue

import sys


# *** NODE SECTION ***
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self, maximum_nodes):  # to initiate head
        self.head = None
        self.last = None
        self.count = 0
        self.maximum_nodes = maximum_nodes

    def enqueue(self, data):  # add node at the end of the queue
        node = Node(data)
        if self.last is None:
            self.head = node
            self.last = self.head
        else:
            self.last.next = node
            self.last.next.prev = self.last
            self.last = self.last.next
        self.count += 1

    def dequeue(self):  # remove first node from the queue
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return temp

    def isempty(self):
        if self.head is None:
            print('Queue is empty.')
        else:
            print('There are nodes in the queue.')

    def isfull(self):
        capacity = round(self.count / self.maximum_nodes * 100)
        print(f"\nUtilised capacity of the queue {capacity}%."
              f"\nRemaining capacity of the queue is {100-capacity}%.")

    def show(self):
        temp = self.last
        while temp is not None:
            print(f"Node:{id(temp)} Data: {temp.data}", end=' ==> ')
            temp = temp.prev
        print('None')


# *** INTRO ***
max_queue = int(input('Enter a number (1 to 10) to '
                      'represent maximum number of nodes in the queue:'))
raw_queue = Queue(max_queue)


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
    raw_queue.isempty()
    print('\nExecuted.')
    go_on()


def IsFull():
    raw_queue.isfull()
    print('\nExecuted.')
    go_on()


def Enqueue():
    if raw_queue.count < max_queue:
        val = input('Enter data you want to add to the queue: ')
        raw_queue.enqueue(val)
    else:
        print(f"Queue is full. You can't add more nodes.")
    go_on()


def Dequeue():
    raw_queue.dequeue()
    print('\nExecuted.')
    go_on()


def Show():
    raw_queue.show()
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
