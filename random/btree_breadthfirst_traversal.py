class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
