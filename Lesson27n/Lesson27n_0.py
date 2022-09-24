# data structure
# linked list


class Node:
    def __init__(self, item):  # Function to initialize the node object
        self.item = item
        self.next = None


b = Node(27)
c = Node(5)
d = Node(10)

b.next = c
c.next = d

print(f"B: item={b.item}\t next:{b.next.__dict__}")
print(f"C: item={c.item}\t next:{c.next.__dict__}")
print(f"D: item={d.item}\t next:{d}")


class LinkedList:
    def __init__(self):  # Function to initialize the Linked List object (and head)
        self.head = None

    def add(self, item):  # Function to insert a new node at the beginning
        node = Node(item)
        node.self = self.head
        self.head = node

    def append(self, item):  # Inserts a new node
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def remove(self, item):  # delete the first occurrence of key in linked list
        cur = self.head
        cur_pre = None
        while cur:
            if cur.item == item:
                if cur_pre is None:
                    self.head = cur.next
                    break
                else:
                    cur_pre.next = cur.next
            cur_pre = cur
            cur = cur.next

    def is_empty(self):
        return self.head is None

    def insert(self, position, item):
        if position == 0:
            self.add(item)
        elif 0 < position <= self.len():
            node = Node(item)
            i = 0
            cur = self.head
            while cur:
                if position == i + 1:
                    node.next = cur.next
                    cur.next = node
                cur = cur.next
                i += 1
        else:
            print('Error')

    def search(self, item):
        cur = self.head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def travel(self):  # This function prints contents of linked list
        cur = self.head
        while cur:
            print(f"Node: {id(cur)} |Item: {cur.item} (next: {id(cur.next)})", end=" ==> ")
            cur = cur.next
        print("None")

    def __str__(self):
        nodes = ""
        cur = self.head
        while cur:
            nodes += str(cur.item) + " "
            cur = cur.next
        return nodes

    def __getitem__(self, item):
        print(f"Hello {item}")

    def len(self):
        cur = self.head
        i = 0
        while cur:
            i += 1
            cur = cur.next
        return i


# create list
ll = LinkedList()

# add nodes
ll.append(5)
ll.append(10)
ll.append(8)
ll.append(15)
ll.append(1)
ll.append(4)

# illustrate chain of nodes
ll.travel()

# remove node
ll.remove(5)

# illustrate chain of nodes after removal
ll.travel()

# search if item in list
check = ll.search(55)
print(check)

#
ll.__getitem__(1)

#
ll.insert(3, -5)
print(ll)

# illustrate chain of nodes after inserting
ll.travel()