# HW on saving logins and passwords using data structure

import csv, sys


# *** NODE SECTION ***
class Node:
    def __init__(self, next=None, prev=None, login=None, password=None):
        self.next = next
        self.prev = prev
        self.login = login
        self.password = password


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_new(self, login, password):  # add node at the end of the list
        new_node = Node(login=login, password=password)
        last = self.head
        new_node.next = None
        self.count += 1
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def del_record(self, login):
        current = self.head
        prev = self.head
        while current:
            if current.login == login:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        self.count -= 1

    def search(self, login):
        temp = self.head
        found = 0
        i = 0

        if temp != None:
            while temp != None:
                i += 1
                if temp.login == login:
                    found += 1
                    break
                temp = temp.next
            if found != 0:
                return i

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def replace_login(self, old_login, new_login):
        current = self.head
        while current is not None:
            if current.login == old_login:
                current.login = new_login
                break
            current = current.next

    def replace_password(self, login, new_password):
        current = self.head
        while current is not None:
            if current.login == login:
                current.password = new_password
                break
            current = current.next

    def return_id(self, login):
        cur = self.head
        current = self.head
        while current is not None:
            if current.login == login:
                return id(cur)

    def get_nth_login(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                l = current.login
                p = current.password
                return l
            count += 1
            current = current.next
        assert False

    def get_nth_password(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                p = current.password
                return p
            count += 1
            current = current.next
        assert False

    def get_nth_id(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                record_id = id(current)
                return record_id
            count += 1
            current = current.next
        assert False

    def print_list(self):
        cur = self.head
        while cur:
            print(f"Record: {id(cur)} | Login: {cur.login} | Password: {cur.password}", end=" ==> ")
            cur = cur.next
        print("None")

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# *** MENU SECTION ***
list_of_users = DoubleLinkedList()  # create list


# load whatever records are currently in DB file
def LoadData():
    try:
        file = open('list.csv', 'r')
        reader = csv.DictReader(file)
        for_import = list(reader)
        file.close()

        # iterate
        for record in for_import:  # looping list
            login = record.get('login')
            password = record.get('password')
            list_of_users.add_new(login, password)

    except Exception as e:
        print(str(e))


def menu():
    LoadData()
    choice = 0
    while choice != 6:
        print(f"\n \t Menu:"
              f"\n[1] Add new record"
              f"\n[2] Remove record"
              f"\n[3] Find record"
              f"\n[4] Edit login"
              f"\n[5] Edit password"
              f"\n[6] Exit"
              f"\n[7] Save")
        choice = int(input(f'\nPlease enter option from the menu: '))
        match choice:
            case 1:
                AddRecord()
            case 2:
                RemoveRecord()
            case 3:
                FindRecord()
            case 4:
                EditLogin()
            case 5:
                EditPassword()
            case 6:
                ExitProgram()
            case 7:
                Migrate()


def AddRecord():
    login = str(input('Enter login: '))
    password = str(input('Enter password: '))
    list_of_users.add_new(login, password)
    print('\nRecord added.')
    GoOn()


def RemoveRecord():
    login = str(input('Enter record login you want to delete from DB: '))
    list_of_users.del_record(login)
    print('\nRecord removed.')
    GoOn()


def FindRecord():
    login = str(input('Which record login you want to find? '))
    try:
        result = list_of_users.search(login)
        if result > 0:
            print(f'\nRecord found, index {result}.')
        else:
            print("\nRecord not found.")
    except TypeError:
        print('Record not found.')
    GoOn()


def EditLogin():
    original_login = str(input('\nEnter record [login] you want to replace: '))
    new_login = str(input(f'Enter [NEW login] you want to replace {original_login} with: '))
    list_of_users.replace_login(original_login, new_login)
    print('\nLogin changed.')
    GoOn()


def EditPassword():
    login = str(input('\nEnter record [login] for which you want to update password: '))
    new_password = str(input(f'Enter [NEW password] you want for {login}: '))
    list_of_users.replace_password(login, new_password)
    print('\nPassword changed.')
    GoOn()


def ExitProgram():
    Migrate()
    print('\nSession terminated.')
    sys.exit()


def PrintList():
    list_of_users.print_list()
    GoOn()


def GoOn():
    print('\nDo you want to continue? [Y/N]')
    selection = str(input('>>>')).lower()
    if selection == 'n':
        ExitProgram()
    else:
        pass


# move data from linkedlist to dict and save to file
for_export = {}


def Migrate():
    max = list_of_users.size()
    for i in range(max):
        login = list_of_users.get_nth_login(i)
        password = list_of_users.get_nth_password(i)
        record_id = list_of_users.get_nth_id(i)
        for_export[record_id] = [login, password]

    try:
        file = open('list.csv', 'w')
        writer = csv.DictWriter(file, fieldnames=['record', 'login', 'password'])
        writer.writeheader()
        for key, items in for_export.items():
            writer.writerow(dict(record=key, login=items[0], password=items[1]))
        file.close()

    except Exception as e:
        print(str(e))


# invoke menu
menu()
