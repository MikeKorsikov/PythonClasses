# data structure (part 3)
# stack (LIFO)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

    def push(self, item):
        node = Node(item)
        if node is None:
            print('Heap overflow')
        node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if self.top is None:
            print('Stack is empty.')

        top = self.top.data
        self.top = self.top.next
        self.count -= 1
        return top

    def get_top(self):
        if self.top is None:
            print('Stack is empty.')
        return self.top.data

    def __str__(self):
        line = ""
        cur = self.top
        while cur is not None:
            line += str(cur.data) + " \n"
            cur = cur.next
        return line



#
st = Stack()
st.push(5)
st.push(7)
st.push(3)

print('All stack elements:')
print(st)

print(f'Top value is: {st.get_top()}')

print("\nRemoving top element:")
st.pop()
print(st)
print(f'Top value is: {st.get_top()}')