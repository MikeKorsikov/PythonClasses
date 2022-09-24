# data structure (part 3)
# queue (FIFO)
'''
# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


#
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()
'''

print('\n *** QUEUE ***')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        node = Node(item)
        if self.last is None:
            self.head = node
            self.last = self.head
        else:
            self.last.next = node
            self.last.next.prev = self.last
            self.last = self.last.next
        self.count += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            value = self.head.data
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.last = None
            self.count -= 1
            return value


    def first(self):
        if self.head is not None:
            return self.head.data
        else:
            return None

    def __str__(self):
        line = 'Queue elements: '
        i = 0
        cur = self.head
        while cur is not None:
            line += f"{i} : {str(cur.data)} \t"
            cur = cur.next
            i += 1
        return line


# create queue
print('Create queue: ')
g = Queue()
print(g)

# add elements
print('\nAdding elements: ')
g.enqueue(5)
g.enqueue(7)
g.enqueue(3)
g.enqueue(6)
print(g)

# remove
print('\nRemove first element:')
g.dequeue()
print(g)

# show first element
print('\nFirst current element:')
print(g.first())

# show number of elements
print('\nCurrent number of elements:')
print(g.size())

# remove all
print('\nRemove all elements:')
g.dequeue()
g.dequeue()
g.dequeue()
g.dequeue()  # to check
print(g)
