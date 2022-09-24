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

    def append(self, data):  # insert at the end of the list
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def size1(self):
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

    def delete1(self, data):
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


# TESTING
print('Creating list: ')
list1 = SinglyLinkedList()

print('Adding nodes: ')
list1.add(100)
list1.add(200)
list1.add(300)
list1.add(400)
list1.add(500)

print(f'\nSize of the list (calling size1 function):')
print(list1.size1())

print(f'\nContent of the nodes in the list (calling iter function):')
for item in list1.iter():
    print(item)

print('\nRemoving FIRST node containing specific data (calling delete function):')
value_to_remove = 100
list1.delete1(value_to_remove)
list1.print_list()
list1.push(value_to_remove)

print('\nRemoving LAST node containing specific data (calling delete function):')
value_to_remove = 500
list1.delete1(value_to_remove)
list1.print_list()
list1.append(value_to_remove)

print('\nSearching item (calling search function):')
value = 900
print(f"{value} in the list - {list1.search(value)}")

print('\nFull list of nodes:')
list1.print_list()

print('\nPushing new node in front (calling push function):')
list1.push(50)
list1.print_list()

print('\nAppending list with new node at the end of the list (calling append function):')
list1.append(600)
list1.print_list()

print('\nReversing list')
list1.reverse()
list1.print_list()

print('\nClearing the list of nodes (calling clear function):')
list1.clear()
print(f'Number of nodes in the list is - {list1.size1()}.')
