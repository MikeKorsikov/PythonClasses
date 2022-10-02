# use getitem and setitem with linked list


class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __getitem__(self, index):
        if 0 <= index < self.count:
            current = self.head
            for i in range(index):
                current = current.next
            return f"Index [{index}] has value [{current.data}]."
        else:
            return f'Index [{index}] is out of range.' \
                   f'\nSelect value between [0] and [{self.count - 1}].'

    def __setitem__(self, index, data):
        if 0 <= index < self.count:
            current = self.head
            for i in range(index):
                current = current.next
            current.data = data
        else:
            return f'Index [{index}] is out of range.' \
                   f'\nSelect value between [0] and [{self.count - 1}].'

    def push_node(self, new_data):  # add node in front of the list
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None
        self.count += 1

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def append_node(self, new_data):  # add node at the end of the list
        new_node = Node(data=new_data)
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

    def print_list(self):  # This function prints contents of linked list
        cur = self.head
        while cur:
            print(f"Node: {id(cur)} |Data: {cur.data} (next: {id(cur.next)})", end=" ==> ")
            cur = cur.next
        print("None")

    def iter(self):
        current = self.head
        while current:
            val = current.login
            current = current.next
            yield val

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Create list and add nodes to the list
list2 = DoubleLinkedList()
list2.push_node(100)
list2.push_node(200)
list2.append_node(50)

# testing __getitem__
print('\nGetting item using method __getitem__:')
print(list2[2])

# testing __setitem__
print('\nSetting item using method __setitem__:')
print('\nList prior change:')
list2.print_list()
list2[2] = 49

print('\nList after change:')
list2.print_list()

print('\nChecking by accessing through __getitem__:')
print(list2[2])
