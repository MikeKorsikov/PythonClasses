# data structure

import sys


# *** NODE SECTION ***
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):  # Inserts a new node at the end by default
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def push(self, data):  # insert in front of the list
        node = Node(data)
        node.next = self.head
        self.head = node

    def append_list(self, data):  # insert at the end of the list
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def delete_node(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

    def removeAllDuplicates(self, data):
        for node in self.iter():
            if data == node:
                self.delete_node(data)

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        self.head = None

    def print_list(self):  # This function prints contents of linked list
        cur = self.head
        while cur:
            print(f"Node: {id(cur)} |Data: {cur.data} (next: {id(cur.next)})", end=" ==> ")
            cur = cur.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def replace_data(self, old_data, new_data):
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
                break
            current = current.next


try:
    # *** INITIATION ***
    number_of_digits = int(input('Enter number of digits you want to submit: '))
    raw_list = SinglyLinkedList()

    for i in range(number_of_digits):
        number = int(input(f'Enter [{i + 1}] number:'))
        raw_list.append_list(number)

    print(f'\nThe list of numbers:')
    raw_list.print_list()


    # *** MENU SECTION ***

    def menu():
        choice = 0
        while choice != 6:
            print(f"\n \t Menu:"
                  f"\n[1] Add new number"
                  f"\n[2] Delete number"
                  f"\n[3] Display list (*submenu)"
                  f"\n[4] Check if number is in the list"
                  f"\n[5] Replace number (*submenu)"
                  f"\n[0] Exit")
            choice = int(input(f'\nPlease enter option from the menu: '))

            match choice:
                case 1:
                    add_record()
                case 2:
                    remove_record()
                case 3:
                    display_all_records()
                case 4:
                    check_records()
                case 5:
                    replace_record()
                case 0:
                    exit_program()


    def add_record():
        val = int(input('Enter number to be added to the list:'))
        if raw_list.search(val):
            print(f'Value {val} is already in the list.')
        else:
            raw_list.append_list(val)
            print('\nRecord added.')
        go_on()


    def remove_record():
        val = int(input('Enter number to be removed from the list:'))
        if raw_list.search(val) is True:
            raw_list.removeAllDuplicates(val)
            print(f'\nRecord removed.')
        else:
            print(f"There is no {val} in the list.")
        go_on()


    def display_all_records():
        print(f'\n[1] Original order'
              f'\n[2] Reverse order')
        selection = int(input(f'\nPlease enter option from the menu: '))
        print(f'\nList of records:')
        if selection == 1:
            raw_list.print_list()
        else:
            raw_list.reverse()
            raw_list.print_list()
            raw_list.reverse()
        go_on()


    def check_records():
        val = int(input('Enter number you want to find in the list:'))
        if raw_list.search(val) is True:
            print(f"\nCheck executed (POSITIVE):"
                  f"\nNumber [{val}] was found in the list.")
        else:
            print(f"\nCheck executed (NEGATIVE):"
                  f"\nNumber [{val}] was not found in the list.")
        go_on()


    def replace_record():
        original_data = int(input('\nEnter number you want to replace in the list:'))
        new_data = int(input(f'Enter NEW number you want to replace {original_data} with:'))
        raw_list.replace_data(original_data, new_data)
        print(f'\nRecord replaced.')
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

except Exception as e:
    print(str(e))
