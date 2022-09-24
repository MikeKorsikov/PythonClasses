# binary trees

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# noinspection PyTypeChecker
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def get_root(self):
        return self.root

    def is_empty(self):
        return self.root is None  # returns True or False

    def add(self, item):
        if self.root is None:
            self.root = Node(item)  # create first node / root
        else:
            self.__add(item, self.root)  # create child to existing tree

    def __add(self, item, node):
        if item < node.item:
            if node.left is not None:
                self.__add(item, node.left)  # recursion looking for left == None
            else:
                node.left = Node(item)  # set left child equal to new node / child
        else:
            if node.right is not None:
                self.__add(item, node.right)  # recursion looking for right == None
            else:
                node.right = Node(item)  # set right child equal to new node / child

    def find(self, item):
        if self.root is not None:
            return self.__find(item, self.root)

    def __find(self, item, node):
        if item == node.item:
            return node.item
        elif item < node.item and node.left is not None:
            return self.__find(item, node.left)
        elif item > node.item and node.right is not None:
            return self.__find(item, node.right)

    # def __find_node(self, node):
    #     while node.left != None:
    #         node = node.left
    #     return node

    def delete_leaf(self, item):
        if self.root is not None:
            return self.__delete_leaf(item, self.root)
        else:
            return None

    def __delete_leaf(self, item, node):
        if node.item > item:
            node.left = self.__delete(item, node.left)

        elif node.item < item:
            node.right = self.__delete(item, node.right)

        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right

            temp = node.right
            temp_item = temp.item
            while temp.left:
                temp = temp.left
                temp_item = temp.item
            node.right = self.__delete_leaf(node.item, node.right)

        return node


    def PrintTree(self):
        root = self.root

        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        nlevels = height(root)
        width = pow(2, nlevels + 1)
        q = [(root, 0, width, 'c')]
        levels = []
        while (q):
            node, level, x, align = q.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])
                levels[level].append([node, level, x, align])
                seg = width // (pow(2, level + 1))
                q.append((node.left, level + 1, x - seg, 'l'))
                q.append((node.right, level + 1, x + seg, 'r'))
        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (pow(2, i + 1))
            for n in l:
                valstr = str(n[0].item)
                if n[3] == 'r':
                    linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                    preline = n[2]
                if n[3] == 'l':
                    linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                    preline = n[2] + seg + seg // 2
                pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr)




# create nodes
root = Tree()
root.add(5)
root.add(2)
root.add(7)
root.add(8)
root.PrintTree()
