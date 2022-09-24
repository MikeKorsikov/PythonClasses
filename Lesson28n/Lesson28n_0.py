# data structure


class Node:
    def __init__(self, item):  # Function to initialize the node object
        self.item = item
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):  # Function to initialize the Linked List object (and head)
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head

    def add_front(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.head = node

    def add_back(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove_first(self):
        if self.is_empty():
            print('List empty')
            pass
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove_last(self):
        if self.is_empty():
            print('List empty')
            pass
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            prev_obj = self.tail.prev
            prev_obj.next = None
            self.tail.prev = None
            self.tail = prev_obj

    def remove_key(self, key):
        if self.is_empty():
            print('List empty')
            pass

        cur = self.head
        while cur is not None and cur.item != key:
            cur = cur.next

        if cur is None:
            print(f'Not found {key}')
            return

        prev_obj = cur.prev
        if cur.next is None:
            self.tail = prev_obj

        if prev_obj is None:
            self.head = cur.next
            if self.head is not None:
                self.head.prev = None
            return

        prev_obj.next = cur.next
        cur.prev = None
        cur.next.prev = prev_obj

    def travel(self):
        cur = self.tail

        while cur is not None:
            print(f"{cur.item} => ", end="")
            cur = cur.prev
        print('None')


# create object
d = DoublyLinkedList()
d.add_back(5)
d.add_back(10)
d.add_back(2)

d.travel()

d.add_back(999)

d.travel()